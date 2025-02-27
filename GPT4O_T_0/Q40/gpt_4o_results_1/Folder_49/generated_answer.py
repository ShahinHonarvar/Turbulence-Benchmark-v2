def return_n_smallest_chars(s):
    sorted_chars = sorted(s)
    smallest_chars = sorted_chars[:76]
    return sorted(smallest_chars, reverse=True)