def return_n_smallest_chars(s):
    sorted_s = sorted(s)
    n_smallest_chars = sorted_s[:77]
    sorted_n_smallest_chars = sorted(n_smallest_chars, reverse=True)
    return sorted_n_smallest_chars