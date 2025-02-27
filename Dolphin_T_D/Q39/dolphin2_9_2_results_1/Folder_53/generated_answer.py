def return_n_greatest_chars(s):
    return sorted([c for c in s if c in s][-19:], key=lambda x: s.index(x))