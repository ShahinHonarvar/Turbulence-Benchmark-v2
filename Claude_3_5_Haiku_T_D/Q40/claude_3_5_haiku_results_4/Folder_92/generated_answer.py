def return_n_smallest_chars(s):
    sorted_chars = sorted(set(s))[:63]
    return sorted_chars