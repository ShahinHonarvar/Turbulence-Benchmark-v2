def return_nth_smallest_ascii(s):
    ascii_values = sorted((ord(c) for c in s if 0 <= s.index(c) <= 7))
    return chr(ascii_values[7]) if len(ascii_values) > 7 else None