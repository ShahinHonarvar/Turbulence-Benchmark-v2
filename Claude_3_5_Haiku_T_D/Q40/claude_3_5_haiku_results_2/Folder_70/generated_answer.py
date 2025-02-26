def return_n_smallest_chars(s):
    chars = sorted(list(s))[:2]
    return sorted(chars, reverse=True)