def return_n_greatest_chars(input_string):
    sorted_list = sorted(input_string, key=lambda x: -x)
    return sorted_list[:72]