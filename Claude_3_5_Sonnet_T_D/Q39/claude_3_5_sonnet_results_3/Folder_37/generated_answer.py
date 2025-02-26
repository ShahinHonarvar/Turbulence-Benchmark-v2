def return_n_greatest_chars(s):
    char_list = list(set(s))
    sorted_chars = sorted(char_list, reverse=True)
    return sorted_chars[:26]