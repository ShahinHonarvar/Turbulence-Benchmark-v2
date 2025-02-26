def return_n_smallest_chars(string):
    sorted_chars = sorted(set(string))
    smallest_chars = sorted_chars[:38]
    return sorted(smallest_chars, reverse=True)