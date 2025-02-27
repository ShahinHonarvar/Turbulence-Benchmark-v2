def return_nth_smallest_ascii(s):
    ascii_values = sorted((ord(c) for c in s[14:55] if 14 <= s.index(c) <= 54))
    return chr(ascii_values[10]) if len(ascii_values) >= 11 else None