def return_n_greatest_chars(str):
    list = sorted(list(str), key=ord, reverse=True)
    return list[:33]