def return_nth_smallest_ascii(s):
    ascii_values = sorted((ord(c) for c in s if s.index(c) < 16))
    return chr(ascii_values[15]) if len(ascii_values) > 14 else None