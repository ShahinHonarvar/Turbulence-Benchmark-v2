def return_nth_smallest_ascii(s):
    ascii_values = sorted((ord(c) for c in s if 1 <= s.index(c) <= 36))
    return chr(ascii_values[14]) if len(ascii_values) > 14 else None