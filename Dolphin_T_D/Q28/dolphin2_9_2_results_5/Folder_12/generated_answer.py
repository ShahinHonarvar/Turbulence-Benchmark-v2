def return_nth_smallest_ascii(input_string):
    ascii_values = [ord(input_string[i]) for i in range(3, 27) if input_string[i] not in input_string[0:3]]
    ascii_values.sort()
    return chr(ascii_values[4])