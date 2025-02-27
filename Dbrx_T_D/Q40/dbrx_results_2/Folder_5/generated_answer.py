def return_n_smallest_chars(input_string):
    ascii_list = sorted(list(input_string), key=ord)
    return ascii_list[:46][::-1]