def return_n_smallest_chars(s):
    chars = sorted(list(s))[:45]
    return chars[::-1]