def return_n_smallest_chars(s):
    s_sorted = sorted(s)
    smallest_75_chars = s_sorted[:75]
    smallest_75_chars.reverse()
    return smallest_75_chars