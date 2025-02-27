def return_n_smallest_chars(s):
    sorted_chars = sorted(s)
    smallest_85 = sorted_chars[:85]
    return smallest_85[::-1]