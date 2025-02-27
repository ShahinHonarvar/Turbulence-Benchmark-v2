def return_n_greatest_chars(s):
    s = list(s)
    s.sort(reverse=True)
    s = s[:64]
    s.sort()
    return s