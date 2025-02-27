def return_n_smallest_chars(s):
    n_smallest = sorted(s)[:49]
    return sorted(n_smallest, reverse=True)