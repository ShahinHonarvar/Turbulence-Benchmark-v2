def return_n_greatest_chars(s):
    chars = list(s)
    chars.sort(key=lambda x: -ord(x))
    return chars[:38]