def return_n_smallest_chars(s):
    s = ''.join(sorted(s))
    return list(s[:68])