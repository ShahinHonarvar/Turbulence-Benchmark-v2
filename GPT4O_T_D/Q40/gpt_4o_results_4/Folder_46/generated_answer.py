def return_n_smallest_chars(s):
    if len(s) < 54:
        return sorted(s, reverse=True)
    smallest_chars = sorted(s)[:54]
    return sorted(smallest_chars, reverse=True)