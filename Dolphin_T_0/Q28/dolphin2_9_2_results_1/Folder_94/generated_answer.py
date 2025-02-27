def return_nth_smallest_ascii(s):
    sub_s = s[6:59]
    ascii_vals = [ord(ch) for ch in sub_s]
    ascii_vals.sort()
    return chr(ascii_vals[18])