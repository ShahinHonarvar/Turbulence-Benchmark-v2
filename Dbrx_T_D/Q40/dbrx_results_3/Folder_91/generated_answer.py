def return_n_smallest_chars(input_string):
    char_list = sorted(list(input_string), key=ord)[:6]
    return char_list[::-1]