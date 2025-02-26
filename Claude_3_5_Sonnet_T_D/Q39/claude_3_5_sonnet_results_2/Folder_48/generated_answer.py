def return_n_greatest_chars(input_string):
    char_list = list(set(input_string))
    sorted_chars = sorted(char_list, key=ord, reverse=True)
    return sorted(sorted_chars[:12])