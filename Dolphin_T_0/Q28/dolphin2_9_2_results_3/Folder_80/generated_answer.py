def return_nth_smallest_ascii(s):
    chars = list(s[51:90])
    ascii_vals = [ord(c) for c in chars]
    return chr(ascii_vals[13])