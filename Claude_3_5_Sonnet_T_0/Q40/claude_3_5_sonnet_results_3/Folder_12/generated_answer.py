def return_n_smallest_chars(s):
    sorted_chars = sorted(set(s))
    smallest_chars = sorted_chars[:61]
    return sorted(smallest_chars, reverse=True)