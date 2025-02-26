def return_n_smallest_chars(s):
    chars = list(set(s))
    chars.sort()
    return chars[:49]