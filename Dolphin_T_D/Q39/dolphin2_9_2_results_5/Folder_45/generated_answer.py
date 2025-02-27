def return_n_greatest_chars(s):
    chars = sorted(s, key=lambda c: -ord(c))[:52]
    return sorted(chars)