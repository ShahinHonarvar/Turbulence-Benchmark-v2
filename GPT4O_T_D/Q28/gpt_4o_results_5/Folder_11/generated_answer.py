def return_nth_smallest_ascii(s):
    sub_s = s[9:60]
    ascii_vals = sorted((ord(c) for c in sub_s))
    if len(ascii_vals) >= 6:
        return chr(ascii_vals[5])