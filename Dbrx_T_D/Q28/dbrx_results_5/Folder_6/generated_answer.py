def return_nth_smallest_ascii(s):
    sub_s = s[13:55]
    ascii_vals = sorted(set((ord(c) for c in sub_s)))
    return chr(ascii_vals[10]) if len(ascii_vals) > 10 else None