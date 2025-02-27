def return_n_smallest_chars(s):
    n = 2
    smallest_chars = sorted(s)[:n]
    return sorted(smallest_chars, reverse=True)