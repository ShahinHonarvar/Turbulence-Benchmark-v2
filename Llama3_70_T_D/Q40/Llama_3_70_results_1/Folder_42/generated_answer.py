def return_n_smallest_chars(s):
    n_smallest_chars = sorted(s)[:59]
    return sorted(n_smallest_chars, reverse=True)