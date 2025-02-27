def return_n_greatest_chars(str):
    str2 = sorted(str, key=ord, reverse=True)
    return str2[:32]