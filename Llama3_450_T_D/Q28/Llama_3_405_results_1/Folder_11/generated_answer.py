def return_nth_smallest_ascii(s):
    chars = sorted([c for i, c in enumerate(s) if 9 <= i <= 59])
    ascii_vals = sorted([ord(c) for c in chars])
    return chr(ascii_vals[5])