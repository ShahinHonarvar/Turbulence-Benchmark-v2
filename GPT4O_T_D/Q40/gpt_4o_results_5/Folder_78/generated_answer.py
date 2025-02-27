def return_n_smallest_chars(s):
    sorted_chars = sorted(s)
    n_smallest = sorted_chars[:43]
    return sorted(n_smallest, reverse=True)