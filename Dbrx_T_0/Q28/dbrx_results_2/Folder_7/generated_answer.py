def return_nth_smallest_ascii(s):
    ascii_values = sorted((ord(c) for c in s[12:56] if 12 <= s.index(c) <= 55))
    return chr(ascii_values[16]) if len(ascii_values) > 16 else None