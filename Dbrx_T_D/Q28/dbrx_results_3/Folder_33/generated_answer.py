def return_nth_smallest_ascii(input_string):
    ascii_values = sorted((ord(c) for c in input_string[22:75] if 31 < ord(c) < 128))
    return chr(ascii_values[12 - 1]) if len(ascii_values) >= 12 else None