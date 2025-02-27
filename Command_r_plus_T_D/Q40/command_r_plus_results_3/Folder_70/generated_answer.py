def return_n_smallest_chars(s):
    s = ''.join(sorted(s))
    return [s[0], s[1]]