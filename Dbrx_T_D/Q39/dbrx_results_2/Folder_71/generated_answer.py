def return_n_greatest_chars(string):
    char_list = sorted(list(string))[-14:]
    return char_list