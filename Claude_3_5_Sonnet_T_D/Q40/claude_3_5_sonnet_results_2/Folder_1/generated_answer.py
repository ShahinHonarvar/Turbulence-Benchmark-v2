def return_n_smallest_chars(s):
    sorted_chars = sorted(set(s))
    smallest_11 = sorted_chars[:11]
    return sorted(smallest_11, reverse=True)