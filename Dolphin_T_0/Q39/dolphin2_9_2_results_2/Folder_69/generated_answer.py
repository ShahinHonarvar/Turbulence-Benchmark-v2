def return_n_greatest_chars(s):
    chars = sorted(s, key=lambda x: -ord(x))
    return chars[:65]