def return_n_greatest_chars(s):
    return sorted([ch for ch in s if s.index(ch) < 82], key=lambda x: s.index(x))