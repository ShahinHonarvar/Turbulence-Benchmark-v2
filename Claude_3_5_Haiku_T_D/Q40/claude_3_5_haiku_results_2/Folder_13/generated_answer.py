def return_n_smallest_chars(string):
    sorted_chars = sorted(set(string))[:31]
    return sorted_chars