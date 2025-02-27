def return_n_smallest_chars(s):
    return sorted([min(s)] + [min(s.replace(min(s), '', 1))])