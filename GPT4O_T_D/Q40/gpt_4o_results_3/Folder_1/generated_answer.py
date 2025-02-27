def return_n_smallest_chars(s):
    if len(s) < 11:
        return None
    smallest_chars = sorted(s)[:11]
    return sorted(smallest_chars, reverse=True)