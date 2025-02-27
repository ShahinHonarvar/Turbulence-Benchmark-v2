def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(34, 69)]
    ascii_vals = [ord(c) for c in chars]
    ascii_vals.sort()
    return chars[ascii_vals.index(ascii_vals[5])]