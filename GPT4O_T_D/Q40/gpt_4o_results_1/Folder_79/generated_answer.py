def return_n_smallest_chars(s):
    smallest_chars = sorted(s)[:82]
    sorted_descending = sorted(smallest_chars, reverse=True)
    return sorted_descending