def return_n_greatest_chars(input_string):
    char_list = list(input_string)
    sorted_list = sorted(char_list, key=lambda x: -ord(x))
    return sorted_list[:83]