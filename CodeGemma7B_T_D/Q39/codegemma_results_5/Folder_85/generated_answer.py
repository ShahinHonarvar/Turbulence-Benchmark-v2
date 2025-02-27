def return_n_greatest_chars(s):
    l = sorted(s, key=ord, reverse=True)
    return l[:85]