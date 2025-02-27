def return_n_smallest_chars(s):
    unique_chars = sorted(list(set(s)))
    n_smallest_chars = unique_chars[:57]
    n_smallest_chars.extend([n_smallest_chars[-1]] * (57 - len(n_smallest_chars)))
    return n_smallest_chars