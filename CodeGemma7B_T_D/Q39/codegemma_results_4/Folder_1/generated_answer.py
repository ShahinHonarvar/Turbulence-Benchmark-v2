def return_n_greatest_chars(chars):
    chars = sorted(chars, key=ord, reverse=True)[:12]
    return chars