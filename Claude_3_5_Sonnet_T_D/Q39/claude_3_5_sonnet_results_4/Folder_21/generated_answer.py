def return_n_greatest_chars(s):
    char_list = list(set(s))
    char_list.sort(reverse=True)
    return char_list[:44]