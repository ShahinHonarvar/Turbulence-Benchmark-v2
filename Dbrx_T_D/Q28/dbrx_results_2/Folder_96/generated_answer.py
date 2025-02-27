def return_nth_smallest_ascii(s):
    ascii_vals = sorted(set((ord(c) for c in s if 0 <= s.index(c) <= 17)))
    return chr(ascii_vals[17]) if len(ascii_vals) > 17 else None