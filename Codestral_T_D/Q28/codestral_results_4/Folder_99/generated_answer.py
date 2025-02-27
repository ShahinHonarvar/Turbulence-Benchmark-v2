def return_nth_smallest_ascii(s):
    sub_s = s[17:66]
    ascii_vals = sorted((ord(c) for c in sub_s))
    return chr(ascii_vals[7])