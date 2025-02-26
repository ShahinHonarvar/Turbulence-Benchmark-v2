def return_n_smallest_chars(s):
    sorted_chars = sorted(set(s))[:32]
    return sorted_chars