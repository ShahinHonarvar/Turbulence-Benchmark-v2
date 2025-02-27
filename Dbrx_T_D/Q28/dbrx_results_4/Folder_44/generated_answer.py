def return_nth_smallest_ascii(input_string):
    ascii_values = sorted((ord(c) for c in input_string[20:31] if c.isascii() and c not in ('\t', '\n', '\r')))
    return chr(ascii_values[7]) if len(ascii_values) > 7 else None