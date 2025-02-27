def return_nth_smallest_ascii(s):
    chars = sorted(s[42:60])
    ascii_vals = [ord(c) for c in chars]
    return chr(sorted(ascii_vals)[16])