def return_n_greatest_chars(str):
    l = list(str)
    l.sort(key=ord, reverse=True)
    return l[:2]