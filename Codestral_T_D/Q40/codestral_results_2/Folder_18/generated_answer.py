def return_n_smallest_chars(s):
    s = list(sorted(s))
    return sorted(s[:52], reverse=True)