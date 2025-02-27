def return_nth_smallest_ascii(s):
    ascii_values = sorted((ord(c) for c in set(s) if 0 <= s.index(c) <= 18))
    return chr(ascii_values[12]) if len(ascii_values) > 12 else None