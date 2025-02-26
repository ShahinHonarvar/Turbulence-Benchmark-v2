def return_n_smallest_chars(s):
    smallest_chars = sorted(set(s), key=ord)[:9]
    return sorted(smallest_chars, reverse=True)