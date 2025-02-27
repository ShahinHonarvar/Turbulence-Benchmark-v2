def return_n_smallest_chars(s):
    smallest_chars = sorted(s)[:87]
    return sorted(smallest_chars, reverse=True)