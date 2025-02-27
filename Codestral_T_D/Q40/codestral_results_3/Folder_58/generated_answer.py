def return_n_smallest_chars(chars):
    sorted_chars = sorted(chars)
    smallest_chars = sorted_chars[:49]
    return sorted(smallest_chars, reverse=True)