def return_n_smallest_chars(s):
    n = min(len(s), 43)
    smallest_chars = sorted(s)[:n]
    return sorted(smallest_chars, reverse=True)