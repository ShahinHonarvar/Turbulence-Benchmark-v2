def return_n_smallest_chars(s):
    s = ''.join(sorted(s))
    smallest_chars = s[:24]
    return sorted(smallest_chars, reverse=True)