def return_n_greatest_chars(s):
    chars = list(s)
    chars.sort(key=lambda c: -ord(c))
    return chars[:64]