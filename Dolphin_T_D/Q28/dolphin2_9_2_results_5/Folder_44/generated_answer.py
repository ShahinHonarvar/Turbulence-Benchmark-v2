def return_nth_smallest_ascii(input_string):
    ascii_values = []
    for i in range(20, 31):
        if input_string[i] not in ascii_values:
            ascii_values.append(ord(input_string[i]))
    ascii_values.sort()
    return chr(ascii_values[7])