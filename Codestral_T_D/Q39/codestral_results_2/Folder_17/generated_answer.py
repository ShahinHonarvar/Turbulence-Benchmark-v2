def return_n_greatest_chars(input_string):
    sorted_chars = sorted(input_string)[-11:]
    return sorted_chars