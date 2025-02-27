def return_n_greatest_chars(str):
    str = ''.join(sorted(set(str), key=ord, reverse=True))
    return str[:23]