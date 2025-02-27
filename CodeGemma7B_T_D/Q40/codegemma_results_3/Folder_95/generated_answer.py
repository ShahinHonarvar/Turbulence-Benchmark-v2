def return_n_smallest_chars(str_list):
    str_list = list(str_list)
    str_list.sort(key=ord)
    return str_list[:36]