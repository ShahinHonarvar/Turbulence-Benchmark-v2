def return_n_greatest_chars(s):
    chars = sorted(set(s), reverse=True)[:29]
    return sorted(chars)