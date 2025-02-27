def return_nth_smallest_ascii(s):
    chars = [c for i, c in enumerate(s) if 6 <= i <= 58]
    ascii_vals = [ord(c) for c in chars]
    ascii_vals.sort()
    return chr(ascii_vals[18])