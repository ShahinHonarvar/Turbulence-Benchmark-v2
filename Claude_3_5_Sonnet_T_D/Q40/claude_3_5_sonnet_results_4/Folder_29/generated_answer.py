def return_n_smallest_chars(s):
    chars = list(set(s))
    smallest_chars = sorted(chars)[:23]
    return sorted(smallest_chars, reverse=True)