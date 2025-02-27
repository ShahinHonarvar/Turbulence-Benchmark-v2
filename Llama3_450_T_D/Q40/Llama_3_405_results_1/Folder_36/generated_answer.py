def return_n_smallest_chars(s):
    unique_chars = sorted(set(s))
    return sorted(unique_chars)[:32]