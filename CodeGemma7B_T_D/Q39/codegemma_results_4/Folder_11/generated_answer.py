def return_n_greatest_chars(str):
    str_list = sorted(str, key=ord, reverse=True)
    return str_list[:17]