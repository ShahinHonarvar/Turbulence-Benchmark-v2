def return_n_smallest_chars(s):
    sorted_chars = sorted(s)
    smallest_n_chars = sorted_chars[:90]
    return sorted(smallest_n_chars, reverse=True)