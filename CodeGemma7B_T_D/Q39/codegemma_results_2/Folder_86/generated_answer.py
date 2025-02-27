def return_n_greatest_chars(str):
    str_to_list = list(str)
    str_to_list.sort(reverse=True)
    return str_to_list[:34]