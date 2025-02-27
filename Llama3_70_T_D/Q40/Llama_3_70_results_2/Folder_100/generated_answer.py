def return_n_smallest_chars(s):
    s = ''.join(sorted(s)[:72])
    return sorted(s, reverse=True)