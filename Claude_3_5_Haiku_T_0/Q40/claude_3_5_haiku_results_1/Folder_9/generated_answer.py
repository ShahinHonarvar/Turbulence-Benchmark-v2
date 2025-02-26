def return_n_smallest_chars(s):
    sorted_chars = sorted(set(s))[:20]
    return sorted_chars