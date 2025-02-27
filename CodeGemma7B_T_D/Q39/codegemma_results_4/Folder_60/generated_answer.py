def return_n_greatest_chars(s):
    f = list(s)
    f.sort(key=ord, reverse=True)
    return f[:28]