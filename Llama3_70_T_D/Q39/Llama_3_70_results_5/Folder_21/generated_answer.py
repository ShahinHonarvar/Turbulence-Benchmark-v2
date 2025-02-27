def return_n_greatest_chars(s):
    return sorted(s, key=lambda x: (s.count(x), x), reverse=True)[:44]