def return_n_smallest_chars(s):
    sorted_chars = sorted(set(s))
    smallest_39 = sorted_chars[:39]
    return sorted(smallest_39, reverse=True)