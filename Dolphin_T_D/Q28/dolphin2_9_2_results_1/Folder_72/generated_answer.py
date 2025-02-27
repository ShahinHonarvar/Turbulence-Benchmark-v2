def return_nth_smallest_ascii(input_string):
    ascii_values = [ord(input_string[i]) for i in range(33, 61)]
    ascii_values.sort()
    return chr(ascii_values[17])