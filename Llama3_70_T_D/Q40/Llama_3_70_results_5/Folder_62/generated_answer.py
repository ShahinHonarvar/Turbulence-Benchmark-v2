def return_n_smallest_chars(s):
    s_sorted = sorted(s)
    n_smallest = s_sorted[:84]
    return sorted(n_smallest, reverse=True)