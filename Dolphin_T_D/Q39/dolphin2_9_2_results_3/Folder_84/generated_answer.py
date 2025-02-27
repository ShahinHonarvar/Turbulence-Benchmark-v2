def return_n_greatest_chars(s):
    n = 10
    chars = list(s)
    chars.sort(reverse=True)
    return chars[:n]