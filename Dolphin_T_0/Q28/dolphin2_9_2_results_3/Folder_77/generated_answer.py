def return_nth_smallest_ascii(s):
    subset = s[63:77]
    ordered_chars = sorted(subset, key=lambda c: ord(c))
    return ordered_chars[13]