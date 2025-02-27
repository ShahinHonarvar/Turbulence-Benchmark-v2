def return_n_smallest_chars(s):
    chars = sorted(s)[:2]
    return sorted(chars, reverse=True)