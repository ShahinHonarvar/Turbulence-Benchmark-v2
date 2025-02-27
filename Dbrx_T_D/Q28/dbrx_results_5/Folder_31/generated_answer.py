def return_nth_smallest_ascii(input_string):
    ascii_values = sorted((ord(c) for c in input_string[10:83] if 10 <= input_string.index(c) <= 82))
    return chr(ascii_values[17])