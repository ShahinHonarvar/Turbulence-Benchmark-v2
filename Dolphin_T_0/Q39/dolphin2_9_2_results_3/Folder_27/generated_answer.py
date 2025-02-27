def return_n_greatest_chars(s):
    char_list = sorted(list(s), reverse=True)[:82]
    char_list.sort()
    return char_list