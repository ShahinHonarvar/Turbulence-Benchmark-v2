def return_nth_smallest_ascii(s):
    ascii_vals = sorted((ord(c) for c in s if 60 <= s.index(c) <= 83))
    return chr(ascii_vals[13]) if len(ascii_vals) > 13 else None