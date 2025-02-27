def return_nth_smallest_ascii(s):
    ascii_values = sorted((ord(c) for c in s if s.index(c) < 19))
    return chr(ascii_values[18]) if len(ascii_values) > 18 else None