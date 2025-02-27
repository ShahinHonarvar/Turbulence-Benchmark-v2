def return_n_smallest_chars(s):
    chars = list(s)
    chars.sort()
    chars = chars[:20]
    return chars