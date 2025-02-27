def return_n_smallest_chars(s):
    return sorted([min(s), sorted(s)[1]])