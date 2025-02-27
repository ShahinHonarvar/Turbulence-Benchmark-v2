def return_n_smallest_chars(s):
    s_sorted = sorted(s)
    smallest_84_chars = s_sorted[:84]
    return smallest_84_chars[::-1]