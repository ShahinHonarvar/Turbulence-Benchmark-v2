def return_nth_smallest_ascii(s):
    ascii_vals = sorted((ord(c) for c in s if 12 <= s.index(c) <= 87))
    return chr(ascii_vals[16]) if len(ascii_vals) > 16 else None