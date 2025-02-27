def return_n_greatest_chars(s):
    n = 12
    chars = list(s)
    chars.sort(reverse=True)
    return chars[:n]