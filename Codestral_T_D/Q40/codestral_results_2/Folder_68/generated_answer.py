def return_n_smallest_chars(string):
    sorted_chars = sorted(string)
    smallest_chars = sorted_chars[:89]
    sorted_smallest_chars = sorted(smallest_chars, reverse=True)
    return sorted_smallest_chars