def return_n_greatest_chars(s):
    chars = sorted(list(s), reverse=True)[:7]
    return sorted(chars)