def return_n_smallest_chars(s):
    s = sorted(s)[:16]
    return sorted(s, reverse=True)