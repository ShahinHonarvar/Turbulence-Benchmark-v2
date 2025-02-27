def return_n_smallest_chars(input_string):
    input_string_list = list(input_string)
    sorted_list = sorted(input_string_list, key=lambda x: ord(x))
    return_list = sorted_list[:44]
    return_list.reverse()
    return return_list