def return_nth_smallest_ascii(s):
    ascii_values = sorted((ord(c) for c in s if 17 <= s.index(c) <= 34))
    return chr(ascii_values[17]) if len(ascii_values) > 17 else None