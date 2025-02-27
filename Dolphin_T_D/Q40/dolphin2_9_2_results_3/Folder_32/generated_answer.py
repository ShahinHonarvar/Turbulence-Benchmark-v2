def return_n_smallest_chars(s):
    chars = list(s)
    chars.sort(key=lambda c: ord(c))
    return chars[:8]