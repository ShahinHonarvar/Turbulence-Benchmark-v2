def return_n_smallest_chars(c):
    return sorted(c, key=ord, reverse=True)[:77]