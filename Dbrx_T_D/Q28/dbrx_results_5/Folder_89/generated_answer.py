def return_nth_smallest_ascii(char_string):
    ascii_values = sorted((ord(c) for c in char_string if 24 <= char_string.index(c) <= 71))
    return chr(ascii_values[7]) if len(ascii_values) > 7 else None