def return_n_smallest_chars(s):
    sorted_chars = sorted(set(s))
    smallest_16 = sorted_chars[:16]
    return sorted(smallest_16, reverse=True)