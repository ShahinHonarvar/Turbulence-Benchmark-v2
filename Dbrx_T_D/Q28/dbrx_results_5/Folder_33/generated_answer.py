def return_nth_smallest_ascii(s):
    ascii_values = sorted((ord(c) for c in s[22:75] if 20 < ord(c) < 127))
    return chr(ascii_values[11]) if len(ascii_values) > 11 else None