def return_n_greatest_chars(string):
    char_list = sorted(string, key=ord, reverse=True)
    return char_list[:49] if len(char_list) >= 49 else char_list