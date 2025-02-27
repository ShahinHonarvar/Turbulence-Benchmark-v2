def return_n_smallest_chars(x):
    return sorted(x, key=ord, reverse=True)[:38]