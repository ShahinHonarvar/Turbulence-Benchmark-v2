def return_nth_smallest_ascii(s):
    sub_s = s[18:46]
    ascii_vals = sorted(map(ord, sub_s))
    return chr(ascii_vals[6])