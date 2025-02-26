def return_n_greatest_chars(string):
    char_list = list(set(string))
    char_list.sort(reverse=True)
    return char_list[:66]