def return_nth_smallest_ascii(s):
    ascii_vals = sorted((ord(c) for c in s if 17 <= s.index(c) <= 65))
    return chr(ascii_vals[8]) if len(ascii_vals) > 8 else None