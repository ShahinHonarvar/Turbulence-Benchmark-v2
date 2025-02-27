def return_n_smallest_chars(input_string):
    input_string_to_list = list(input_string)
    input_string_to_list.sort(key=ord)
    return input_string_to_list[:32]