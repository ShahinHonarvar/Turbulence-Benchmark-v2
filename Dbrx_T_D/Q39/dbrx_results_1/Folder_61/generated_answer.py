def return_n_greatest_chars(input_string):
    input_string_list = list(input_string)
    input_string_list.sort(reverse=True)
    return input_string_list[:66]