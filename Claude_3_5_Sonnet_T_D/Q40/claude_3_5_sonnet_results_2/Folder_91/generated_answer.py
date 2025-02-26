def return_n_smallest_chars(string):
    sorted_chars = sorted(string)
    smallest_chars = sorted_chars[:6]
    return sorted(smallest_chars, reverse=True)