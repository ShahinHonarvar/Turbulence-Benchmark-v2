def return_n_greatest_chars(my_str):
    my_list = list(my_str)
    my_list.sort(key=ord, reverse=True)
    return my_list[:52]