def return_n_greatest_chars(input_string):
    input_list = sorted(list(input_string))
    input_list.reverse()
    return input_list[:31]