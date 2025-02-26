def return_n_smallest_chars(input_string):
    char_list = list(set(input_string))
    char_list.sort()
    return char_list[:28]