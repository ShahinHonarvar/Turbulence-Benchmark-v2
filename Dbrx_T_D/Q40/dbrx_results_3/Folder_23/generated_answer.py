def return_n_smallest_chars(input_string):
    chars_list = sorted(input_string, key=ord)
    return chars_list[:46]