def return_n_greatest_chars(input_str):
    char_list = list(input_str)
    char_list.sort(reverse=True)
    return char_list[:68]