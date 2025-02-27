def return_nth_smallest_ascii(s):
    subset = s[29:48]
    ascii_vals = [ord(ch) for ch in subset]
    ascii_vals.sort()
    return chr(ascii_vals[6])