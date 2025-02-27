def return_n_greatest_chars(str):
    str_list = list(str)
    str_list.sort(key=lambda x: ord(x), reverse=True)
    return str_list[:61]