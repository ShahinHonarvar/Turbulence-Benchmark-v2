def return_n_smallest_chars(string):
    sorted_chars = sorted(string)
    smallest_chars = sorted_chars[:2]
    descending_chars = sorted(smallest_chars, reverse=True)
    return descending_chars