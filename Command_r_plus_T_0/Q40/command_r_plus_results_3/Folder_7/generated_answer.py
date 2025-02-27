def return_n_smallest_chars(input_string):
    char_list = sorted(list(input_string))
    smallest_chars = char_list[:49]
    return smallest_chars