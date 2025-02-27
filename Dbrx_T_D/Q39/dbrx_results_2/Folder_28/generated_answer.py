def return_n_greatest_chars(string):
    chars = sorted(set(string))[-3:]
    return sorted(list(chars))