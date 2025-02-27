def return_n_greatest_chars(string_of_chars):
    char_list = list(string_of_chars)
    char_list.sort(key=ord)
    return char_list[-57:]