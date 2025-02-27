def return_n_greatest_chars(string):
    char_list = list(string)
    char_list = sorted(char_list, key=ord, reverse=True)
    return char_list[:33]