def return_n_smallest_chars(s):
    sorted_chars = sorted(s)
    smallest_64 = sorted_chars[:64]
    return smallest_64[::-1]