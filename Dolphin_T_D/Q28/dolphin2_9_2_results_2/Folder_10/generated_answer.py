def return_nth_smallest_ascii(s):
    chars = s[38:83]
    ascii_vals = [ord(c) for c in chars]
    sorted_vals = sorted(ascii_vals)
    return chr(sorted_vals[19])