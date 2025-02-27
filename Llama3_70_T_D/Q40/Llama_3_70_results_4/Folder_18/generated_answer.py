def return_n_smallest_chars(s):
    s = list(s)
    s.sort()
    s = s[:52]
    s.sort(reverse=True)
    return s