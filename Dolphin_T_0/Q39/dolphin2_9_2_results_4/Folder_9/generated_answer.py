def return_n_greatest_chars(string):
    chars = list(string)
    chars.sort(key=lambda x: -ord(x))
    return chars[:20]