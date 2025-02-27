def return_n_greatest_chars(char_str):
    char_list = list(char_str)
    char_list.sort(key=ord, reverse=True)
    return char_list[:84]