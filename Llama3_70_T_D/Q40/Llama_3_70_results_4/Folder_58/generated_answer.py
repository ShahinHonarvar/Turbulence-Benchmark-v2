def return_n_smallest_chars(s):
    smallest_chars = sorted(s, key=lambda c: c)[:49]
    return sorted(smallest_chars, reverse=True)