def return_n_greatest_chars(str):
    str_list = list(str)
    str_list.sort(key=ord, reverse=True)
    return str_list[0:35]