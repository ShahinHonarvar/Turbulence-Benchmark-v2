def return_n_greatest_chars(s):
    s = list(s)
    s.sort()
    return s[-52:][::-1]