def return_n_greatest_chars(s):
    chars = sorted(s, key=lambda c: -ord(c))[:69]
    return sorted(chars)