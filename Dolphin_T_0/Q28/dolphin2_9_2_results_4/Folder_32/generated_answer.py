def return_nth_smallest_ascii(s):
    chars = s[14:67]
    ascii_vals = [ord(c) for c in chars]
    ascii_vals.sort()
    return chars[ascii_vals.index(ascii_vals[7])]