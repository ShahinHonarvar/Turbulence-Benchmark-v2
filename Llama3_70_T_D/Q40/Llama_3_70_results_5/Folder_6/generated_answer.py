def return_n_smallest_chars(s):
    sorted_chars = sorted(s)
    n_smallest_chars = sorted_chars[:47]
    return sorted(n_smallest_chars, reverse=True)