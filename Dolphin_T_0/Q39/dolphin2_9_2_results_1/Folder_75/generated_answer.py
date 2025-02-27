def return_n_greatest_chars(s):
    chars = list(s)
    chars.sort()
    return chars[-2:]