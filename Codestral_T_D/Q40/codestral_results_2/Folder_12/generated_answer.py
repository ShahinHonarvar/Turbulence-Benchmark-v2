def return_n_smallest_chars(s):
    sorted_chars = sorted(s)
    n_smallest_chars = sorted_chars[:61]
    n_smallest_chars.reverse()
    return n_smallest_chars