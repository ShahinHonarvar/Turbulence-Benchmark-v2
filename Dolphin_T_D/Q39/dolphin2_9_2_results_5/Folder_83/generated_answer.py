def return_n_greatest_chars(s):
    chars = sorted(list(s), reverse=True)[:38]
    return sorted(chars, reverse=True)