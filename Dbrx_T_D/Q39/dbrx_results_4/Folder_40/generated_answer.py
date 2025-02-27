def return_n_greatest_chars(input_string):
    chars_list = list(input_string)
    sorted_list = sorted(chars_list, reverse=True)[:7]
    return sorted_list