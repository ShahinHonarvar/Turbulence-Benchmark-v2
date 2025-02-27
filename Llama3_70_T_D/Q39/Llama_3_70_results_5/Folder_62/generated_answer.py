def return_n_greatest_chars(s):
    s = list(s)
    s.sort(reverse=True)
    return s[:84]