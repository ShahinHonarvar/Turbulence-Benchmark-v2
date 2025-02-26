def return_n_smallest_chars(s):
    sorted_chars = sorted(set(s))
    smallest_chars = sorted_chars[:68]
    return sorted(smallest_chars, reverse=True)