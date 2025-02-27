def return_nth_smallest_ascii(char_string):
    ascii_values = sorted((ord(c) for c in char_string if 67 <= char_string.index(c) <= 77))
    return chr(ascii_values[6]) if len(ascii_values) > 6 else None