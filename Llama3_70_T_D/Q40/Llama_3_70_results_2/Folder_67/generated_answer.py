def return_n_smallest_chars(s):
    s = sorted(s)
    n = min(66, len(s))
    return s[:n]