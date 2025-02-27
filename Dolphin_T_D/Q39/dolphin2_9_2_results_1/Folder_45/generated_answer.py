def return_n_greatest_chars(s):
    s = list(set(s))
    s.sort(reverse=True, key=lambda x: ord(x))
    return s[:52]