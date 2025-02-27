def return_nth_smallest_ascii(s):
    chars = sorted(s[6:59])
    ascii_vals = [ord(c) for c in chars]
    return chr(sorted(ascii_vals)[18])