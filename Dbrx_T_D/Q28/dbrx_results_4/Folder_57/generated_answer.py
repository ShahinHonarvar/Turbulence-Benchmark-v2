def return_nth_smallest_ascii(input_string):
    ascii_values = sorted((ord(c) for c in input_string[17:35] if ord('a') <= ord(c) <= ord('z')))
    return chr(ascii_values[17])