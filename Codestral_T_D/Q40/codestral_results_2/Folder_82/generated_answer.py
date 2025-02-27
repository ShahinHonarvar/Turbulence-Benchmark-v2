def return_n_smallest_chars(s):
    n = min(60, len(s))
    smallest_chars = sorted(s)[:n]
    return smallest_chars