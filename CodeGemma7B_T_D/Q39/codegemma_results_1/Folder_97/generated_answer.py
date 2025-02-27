def return_n_greatest_chars(my_str):
    sorted_list = sorted(my_str, key=ord)
    return sorted_list[-38:]