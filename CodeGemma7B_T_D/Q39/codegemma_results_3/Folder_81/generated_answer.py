def return_n_greatest_chars(str_chars):
    str_chars = sorted(str_chars, key=ord, reverse=True)
    return str_chars[:64]