def return_n_greatest_chars(str):
    l = sorted(str, key=ord, reverse=True)
    return l[:90]