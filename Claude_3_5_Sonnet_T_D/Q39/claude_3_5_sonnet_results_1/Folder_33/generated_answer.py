def return_n_greatest_chars(string):
    char_list = list(set(string))
    sorted_chars = sorted(char_list, reverse=True)
    return sorted_chars[:36]