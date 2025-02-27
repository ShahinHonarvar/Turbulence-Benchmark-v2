def return_n_smallest_chars(s):
    return sorted(list(s), key=ord, reverse=True)[:90]