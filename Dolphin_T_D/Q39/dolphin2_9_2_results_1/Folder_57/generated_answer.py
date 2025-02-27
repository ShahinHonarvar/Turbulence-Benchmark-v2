def return_n_greatest_chars(input_str):
    char_list = list(input_str)
    sorted_list = sorted(char_list, reverse=True)[:29]
    return sorted_list