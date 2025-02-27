def return_n_greatest_chars(str):
    str = list(str)
    str.sort(key=ord, reverse=True)
    return str[:16]