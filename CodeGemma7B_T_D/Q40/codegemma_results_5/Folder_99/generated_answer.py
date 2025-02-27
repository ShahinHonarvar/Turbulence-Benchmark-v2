def return_n_smallest_chars(str):
    str_list = list(str)
    str_list.sort(key=ord, reverse=True)
    return str_list[:35]