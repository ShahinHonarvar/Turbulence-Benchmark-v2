def return_n_greatest_chars(s):
    chars = list(s)
    chars.sort(reverse=True, key=ord)
    return chars[:85]