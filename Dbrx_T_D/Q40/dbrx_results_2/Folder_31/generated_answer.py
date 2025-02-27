def return_n_smallest_chars(string):
    sorted_chars = sorted(list(string))
    n_smallest_chars = sorted_chars[:70]
    n_smallest_chars = sorted(n_smallest_chars, reverse=True)
    return n_smallest_chars