def return_n_greatest_chars(s):
    chars = list(s)
    chars.sort(key=lambda x: x, reverse=True)
    return chars[:11]