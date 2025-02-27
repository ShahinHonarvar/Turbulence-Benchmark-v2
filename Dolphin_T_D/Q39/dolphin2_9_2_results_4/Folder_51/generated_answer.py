def return_n_greatest_chars(s):
    chars = sorted(list(s), reverse=True)
    return chars[:45]