def return_n_smallest_chars(s):
    smallest_chars = sorted([char for char in s])[:65]
    return sorted(smallest_chars, reverse=True)