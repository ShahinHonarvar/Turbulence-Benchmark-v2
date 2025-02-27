def return_nth_smallest_ascii(input_string):
    ascii_values = sorted((ord(c) for c in input_string[6:59] if 6 <= input_string.index(c) <= 58))[18]
    return chr(ascii_values)