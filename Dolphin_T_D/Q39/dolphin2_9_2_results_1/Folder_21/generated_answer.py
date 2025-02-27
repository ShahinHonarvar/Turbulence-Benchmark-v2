def return_n_greatest_chars(s):
    chars = list(s)
    chars.sort(reverse=True)
    chars = chars[:44]
    return chars