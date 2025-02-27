def return_nth_smallest_ascii(s):
    chars = sorted(s[10:83])
    ascii_vals = [ord(c) for c in chars]
    return chr(sorted(ascii_vals)[17])