def return_n_smallest_chars(s):
    s_sorted = sorted(s)
    smallest_11_chars = s_sorted[:11]
    smallest_11_chars.reverse()
    return smallest_11_chars