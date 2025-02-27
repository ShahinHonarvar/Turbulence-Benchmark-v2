def return_n_greatest_chars(s):
    chars = list(s)
    n = 87
    chars.sort(reverse=True)
    return chars[:n]