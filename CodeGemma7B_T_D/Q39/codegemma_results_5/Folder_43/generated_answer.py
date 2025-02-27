def return_n_greatest_chars(str):
    str_list = list(str)
    str_list.sort(reverse=True)
    str_list = str_list[0:56]
    return str_list