def return_n_greatest_chars(s):
    s = sorted(s, reverse=True)
    s = s[:49]
    s = sorted(s)
    return s