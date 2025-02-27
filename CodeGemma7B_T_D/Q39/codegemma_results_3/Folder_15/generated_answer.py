def return_n_greatest_chars(str):
    char_list = list(str)
    char_list.sort(key=ord)
    return char_list[-57:]