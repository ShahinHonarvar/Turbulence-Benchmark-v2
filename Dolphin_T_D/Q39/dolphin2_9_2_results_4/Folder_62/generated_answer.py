def return_n_greatest_chars(string):
    char_list = list(string)
    char_list.sort(key=lambda x: -x)
    return char_list[:84]