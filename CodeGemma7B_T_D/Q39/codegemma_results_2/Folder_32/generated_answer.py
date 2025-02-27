def return_n_greatest_chars(str):
    list = sorted(str, key=ord, reverse=True)
    return list[:8]