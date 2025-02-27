def return_n_smallest_chars(s):
    s = sorted(s)
    n_smallest = s[:90]
    return sorted(n_smallest, reverse=True)