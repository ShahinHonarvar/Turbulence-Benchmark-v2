def return_n_greatest_chars(string):
    chars = sorted(list(set(string)))
    return chars[-64:]