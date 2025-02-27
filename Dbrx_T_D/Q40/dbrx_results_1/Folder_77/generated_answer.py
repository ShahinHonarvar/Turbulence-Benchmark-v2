def return_n_smallest_chars(input_string):
    input_list = sorted(list(set(input_string)))
    if len(input_list) < 47:
        return input_list
    else:
        return input_list[:47]