def return_n_smallest_chars(s):
    unique_chars = sorted(list(set(s)))
    n_smallest_chars = unique_chars[:32]
    n_smallest_chars += [n_smallest_chars[-1]] * (32 - len(n_smallest_chars))
    return sorted(n_smallest_chars)