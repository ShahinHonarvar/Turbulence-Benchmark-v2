def return_n_smallest_chars(s):
    s_sorted = sorted(s)
    n_smallest_chars = s_sorted[:13]
    n_smallest_chars.sort(reverse=True)
    return n_smallest_chars