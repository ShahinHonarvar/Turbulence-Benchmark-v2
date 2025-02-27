def return_nth_smallest_ascii(s):
    ascii_values = sorted((ord(c) for c in set(s) if s.index(c) <= 8 and 0 <= s.index(c)))
    return chr(ascii_values[8]) if len(ascii_values) > 8 else None