def return_n_smallest_chars(s):
    chars = sorted([c for c in s])
    return chars[:8]