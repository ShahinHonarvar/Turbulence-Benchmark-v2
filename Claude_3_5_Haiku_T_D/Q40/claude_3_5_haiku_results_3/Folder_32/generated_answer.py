def return_n_smallest_chars(s):
    sorted_chars = sorted(set(s))[:8]
    return sorted_chars