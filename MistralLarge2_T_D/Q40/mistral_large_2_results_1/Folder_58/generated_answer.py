def return_n_smallest_chars(s):
    sorted_chars = sorted(s)[:49]
    return sorted(sorted_chars, reverse=True)