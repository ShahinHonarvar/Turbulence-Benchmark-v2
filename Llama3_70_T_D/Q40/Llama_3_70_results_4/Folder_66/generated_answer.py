def return_n_smallest_chars(s):
    s = sorted(s, key=lambda c: (c.islower(), c))
    return sorted(s[:33], reverse=True)