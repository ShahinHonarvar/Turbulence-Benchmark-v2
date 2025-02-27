def return_n_smallest_chars(s):
    unique_chars = sorted(set(s))
    smallest_chars = unique_chars[:66]
    return sorted(smallest_chars, reverse=True)