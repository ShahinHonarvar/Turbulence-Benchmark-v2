def return_nth_smallest_ascii(s):
    ascii_values = sorted((ord(c) for c in s if 0 <= s.index(c) <= 17))
    return chr(ascii_values[17]) if len(ascii_values) > 17 else None