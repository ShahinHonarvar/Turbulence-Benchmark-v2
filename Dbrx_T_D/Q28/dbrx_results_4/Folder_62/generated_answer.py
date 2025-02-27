def return_nth_smallest_ascii(char_string):
    ascii_vals = sorted((ord(c) for c in char_string[51:79] if char_string.count(c) == 1))
    return chr(ascii_vals[8]) if len(ascii_vals) > 8 else None