def return_nth_smallest_ascii(s):
    ascii_values = sorted((ord(c) for c in s if 5 <= s.index(c) <= 82))
    return chr(ascii_values[15]) if len(ascii_values) > 15 else None