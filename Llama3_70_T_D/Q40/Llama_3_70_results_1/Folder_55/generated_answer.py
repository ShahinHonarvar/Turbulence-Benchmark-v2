def return_n_smallest_chars(s):
    s_sorted = sorted(s)
    n_smallest = s_sorted[:75]
    return sorted(n_smallest, reverse=True)