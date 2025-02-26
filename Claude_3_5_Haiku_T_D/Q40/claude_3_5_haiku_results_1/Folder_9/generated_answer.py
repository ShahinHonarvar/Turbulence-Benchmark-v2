def return_n_smallest_chars(string):
    unique_chars = sorted(set(string))
    return unique_chars[:20]