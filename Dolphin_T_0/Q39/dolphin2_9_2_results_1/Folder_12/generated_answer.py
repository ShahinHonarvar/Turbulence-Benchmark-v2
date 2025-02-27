def return_n_greatest_chars(s):
    chars = sorted(s, key=lambda c: -ord(c))
    return chars[:61]