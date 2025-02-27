def return_n_smallest_chars(s):
    s_sorted = sorted(s)
    smallest_56_chars = s_sorted[:56]
    smallest_56_chars.reverse()
    return smallest_56_chars