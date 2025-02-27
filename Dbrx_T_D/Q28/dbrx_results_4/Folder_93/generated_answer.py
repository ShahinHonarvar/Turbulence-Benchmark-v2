def return_nth_smallest_ascii(s):
    ascii_values = sorted((ord(c) for c in s if 42 <= s.index(c) <= 59))
    return chr(ascii_values[16]) if len(ascii_values) > 16 else None