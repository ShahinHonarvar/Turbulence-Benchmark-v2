def return_n_greatest_chars(s):
    chars = sorted(list(s), key=lambda x: -ord(x))
    return chars[:56]