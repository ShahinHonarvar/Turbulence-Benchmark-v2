def return_n_greatest_chars(string):
    chars = sorted(string, reverse=True)[:64]
    return chars