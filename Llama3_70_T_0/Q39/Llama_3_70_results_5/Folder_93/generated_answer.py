def return_n_greatest_chars(s):
    return sorted(s, key=lambda x: (x, s.index(x)), reverse=True)[:77]