def return_n_greatest_chars(input_string):
    char_list = sorted(list(set(input_string)))[-66:]
    return sorted(char_list, reverse=True)