def return_n_smallest_chars(input_string):
    input_list = list(input_string)
    input_list.sort(key=lambda x: ord(x))
    return input_list[:61][::-1]