def return_nth_smallest_ascii(s):
    chars = sorted(s[1:47])
    ascii_vals = sorted([ord(c) for c in chars])
    return chr(ascii_vals[12])