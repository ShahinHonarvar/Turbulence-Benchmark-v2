def return_n_smallest_chars(input_string):
    input_list = sorted(list(set(input_string)))
    return input_list[:47]