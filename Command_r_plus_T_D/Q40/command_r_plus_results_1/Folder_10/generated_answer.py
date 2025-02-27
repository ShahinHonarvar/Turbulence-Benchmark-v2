def return_n_smallest_chars(s):
    s_sorted = sorted(s)
    smallest_88_chars = s_sorted[:88]
    return smallest_88_chars[::-1]