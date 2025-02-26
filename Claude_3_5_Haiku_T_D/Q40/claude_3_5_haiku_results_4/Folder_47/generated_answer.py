def return_n_smallest_chars(string):
    smallest_chars = sorted(set(string))[:21]
    return sorted(smallest_chars, reverse=True)