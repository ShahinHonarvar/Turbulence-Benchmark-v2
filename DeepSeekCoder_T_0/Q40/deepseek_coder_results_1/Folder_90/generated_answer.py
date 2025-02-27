def return_n_smallest_chars(s):
    sorted_chars = sorted(s)
    smallest_24 = sorted_chars[:24]
    return smallest_24[::-1]