def return_nth_smallest_ascii(s):
    sub_s = s[12:88]
    ascii_vals = sorted(set((ord(c) for c in sub_s)))
    return chr(ascii_vals[16]) if len(ascii_vals) > 16 else None