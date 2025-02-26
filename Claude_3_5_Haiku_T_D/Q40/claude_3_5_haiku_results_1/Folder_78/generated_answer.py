def return_n_smallest_chars(s):
    sorted_chars = sorted(list(s))[:43]
    return sorted(sorted_chars, reverse=True)