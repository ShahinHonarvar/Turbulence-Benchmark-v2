def return_nth_smallest_ascii(s):
    ascii_values = sorted((ord(c) for c in s[6:59] if 6 <= s.index(c) <= 58))
    return chr(ascii_values[18]) if len(ascii_values) > 18 else None