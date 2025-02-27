def return_n_greatest_chars(str):
    str_list = sorted(str, key=ord)
    return str_list[-19:]