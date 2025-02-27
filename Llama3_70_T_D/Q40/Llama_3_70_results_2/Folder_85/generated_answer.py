def return_n_smallest_chars(s):
    s = sorted(s)
    n_smallest = s[:85]
    return sorted(n_smallest, reverse=True)