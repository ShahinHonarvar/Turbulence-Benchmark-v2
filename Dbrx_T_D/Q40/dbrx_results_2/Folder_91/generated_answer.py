def return_n_smallest_chars(input_str):
    input_str_list = list(input_str)
    input_str_list.sort(key=ord)
    return input_str_list[:6]