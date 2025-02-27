def return_n_greatest_chars(str):
    list = sorted(str, key=ord, reverse=True)[:43]
    return list