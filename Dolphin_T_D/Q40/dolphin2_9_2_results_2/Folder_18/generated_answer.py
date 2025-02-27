def return_n_smallest_chars(chars):
    chars = list(chars)
    chars.sort(key=lambda c: ord(c))
    return chars[:52]