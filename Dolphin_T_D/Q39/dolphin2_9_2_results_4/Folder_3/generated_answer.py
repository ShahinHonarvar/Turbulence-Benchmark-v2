def return_n_greatest_chars(strings):
    chars = sorted(list(strings), key=lambda x: -ord(x))
    return chars[:28]