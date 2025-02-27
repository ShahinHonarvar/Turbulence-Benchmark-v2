def return_n_greatest_chars(chars):
    chars = sorted(chars, key=ord, reverse=True)[:76]
    return chars