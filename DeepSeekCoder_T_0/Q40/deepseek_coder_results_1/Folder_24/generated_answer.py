def return_n_smallest_chars(s):
    sorted_chars = sorted(s)
    smallest_32 = sorted_chars[:32]
    return smallest_32[::-1]