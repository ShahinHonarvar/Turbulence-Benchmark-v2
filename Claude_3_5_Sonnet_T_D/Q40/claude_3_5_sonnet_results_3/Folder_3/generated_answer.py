def return_n_smallest_chars(string):
    char_list = sorted(set(string))[:28]
    return sorted(char_list, reverse=True)