def return_n_greatest_chars(s):
    list = sorted(s, key=ord, reverse=True)[:57]
    return list