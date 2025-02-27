def return_n_greatest_chars(input_string):
    input_set = set(input_string)
    char_list = sorted(input_set, reverse=True)
    return char_list[:76]