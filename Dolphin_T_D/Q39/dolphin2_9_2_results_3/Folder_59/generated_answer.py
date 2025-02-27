def return_n_greatest_chars(input_string):
    char_list = list(input_string)
    char_list.sort(reverse=True)
    return char_list[:13]