def return_nth_smallest_ascii(s):
    ascii_values = sorted((ord(c) for c in set(s[25:89]) if 25 <= s.index(c) <= 88))
    return chr(ascii_values[10]) if len(ascii_values) > 10 else None