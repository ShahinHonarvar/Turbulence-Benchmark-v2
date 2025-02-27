def return_n_smallest_chars(s):
    sorted_chars = sorted(s)
    smallest_35_chars = sorted_chars[:35]
    return sorted(smallest_35_chars, reverse=True)