def return_n_smallest_chars(s):
    char_list = sorted(list(s))[:49]
    char_list = sorted(char_list, reverse=True)
    return char_list