def return_n_smallest_chars(string):
    char_list = sorted(set(string))[:49]
    return sorted(char_list, reverse=True)