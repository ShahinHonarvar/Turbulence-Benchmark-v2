def return_n_greatest_chars(input_string):
    char_list = list(set(input_string))
    sorted_chars = sorted(char_list, reverse=True, key=lambda x: ord(x))
    return sorted_chars[:47]