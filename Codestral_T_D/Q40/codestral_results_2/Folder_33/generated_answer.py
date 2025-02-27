def return_n_smallest_chars(string):
    sorted_chars = sorted(string)
    n_smallest_chars = sorted_chars[:36]
    n_smallest_chars.sort(reverse=True)
    return n_smallest_chars