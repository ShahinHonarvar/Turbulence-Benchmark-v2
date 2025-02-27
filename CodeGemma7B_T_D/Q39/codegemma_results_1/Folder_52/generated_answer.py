def return_n_greatest_chars(chars):
    chars = sorted(chars, key=ord, reverse=True)
    return chars[:68]