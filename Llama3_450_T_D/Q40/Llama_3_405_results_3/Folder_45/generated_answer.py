def return_n_smallest_chars(s):
    unique_chars = sorted(set(s))
    smallest_chars = unique_chars[:52]
    return sorted(smallest_chars)