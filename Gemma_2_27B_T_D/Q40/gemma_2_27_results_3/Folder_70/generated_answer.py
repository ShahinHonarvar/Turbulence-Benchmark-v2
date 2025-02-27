def return_n_smallest_chars(s):
    return sorted([min(s), s[s.index(min(s)) + 1]], reverse=True)