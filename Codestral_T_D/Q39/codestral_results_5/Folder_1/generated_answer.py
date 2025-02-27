def return_n_greatest_chars(input_string):
    sorted_list = sorted(input_string, reverse=True)
    return sorted_list[:11]