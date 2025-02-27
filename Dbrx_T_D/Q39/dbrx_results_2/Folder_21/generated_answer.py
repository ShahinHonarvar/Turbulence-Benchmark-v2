def return_n_greatest_chars(string_of_chars):
    char_list = list(string_of_chars)
    sorted_list = sorted(char_list, key=ord, reverse=True)
    return sorted_list[:44]