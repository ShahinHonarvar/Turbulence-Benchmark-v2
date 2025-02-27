def return_nth_smallest_ascii(in_str):
    chars = in_str[25:78]
    ascii_vals = [ord(c) for c in chars]
    ascii_vals.sort()
    return chars[ascii_vals.index(ascii_vals[15])]