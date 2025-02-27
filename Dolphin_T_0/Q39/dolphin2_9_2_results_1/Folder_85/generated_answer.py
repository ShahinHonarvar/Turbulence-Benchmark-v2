def return_n_greatest_chars(s):
    chars = sorted([char for char in s], reverse=True)
    return chars[:85]