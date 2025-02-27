def return_nth_smallest_ascii(s):
    chars = s[37:60]
    ascii_vals = [ord(c) for c in chars]
    ascii_vals.sort()
    return chars[ascii_vals.index(ascii_vals[5])]