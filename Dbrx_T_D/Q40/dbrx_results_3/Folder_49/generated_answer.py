def return_n_smallest_chars(input_string):
    char_list = list(input_string)
    char_list.sort(key=ord)
    n_smallest_chars = char_list[:76]
    n_smallest_chars.sort(key=ord, reverse=True)
    return n_smallest_chars