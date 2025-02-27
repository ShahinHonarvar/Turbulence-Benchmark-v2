def return_nth_smallest_ascii(s):
    ascii_vals = sorted((ord(c) for i, c in enumerate(s) if 14 <= i <= 35))
    return chr(ascii_vals[10]) if len(ascii_vals) >= 11 else None