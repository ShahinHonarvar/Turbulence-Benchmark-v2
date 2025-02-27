def return_n_smallest_chars(s):
    s = list(s)
    s.sort()
    return sorted(s[:61], reverse=True)