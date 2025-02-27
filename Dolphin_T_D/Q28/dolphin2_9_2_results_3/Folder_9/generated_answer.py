def return_nth_smallest_ascii(s):
    chars = s[10:91]
    ascii_vals = {ord(c): c for c in chars}
    sorted_ascii = sorted(ascii_vals.keys())
    return ascii_vals[sorted_ascii[20 - 1]]