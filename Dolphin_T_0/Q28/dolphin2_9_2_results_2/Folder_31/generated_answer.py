def return_nth_smallest_ascii(s):
    sub = s[10:83]
    ascii_vals = [ord(c) for c in sub]
    sorted_vals = sorted(ascii_vals)
    return sub[ascii_vals.index(sorted_vals[17])]