def return_n_greatest_chars(s):
    return sorted(list(s), key=lambda c: -ord(c))[:70]