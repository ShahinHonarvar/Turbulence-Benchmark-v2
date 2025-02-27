def return_n_greatest_chars(input_string):
    char_list = list(input_string)
    char_list.sort(key=ord, reverse=True)
    return char_list[:35]