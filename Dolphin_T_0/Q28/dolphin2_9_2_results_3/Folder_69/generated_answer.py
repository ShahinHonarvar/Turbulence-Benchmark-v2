def return_nth_smallest_ascii(s):
    chars = s[67:78]
    ascii_vals = {ord(c): c for c in chars}
    ascii_vals = {k: v for k, v in sorted(ascii_vals.items())}
    return list(ascii_vals.values())[6]