def return_n_smallest_chars(string):
    char_list = sorted(set(string))[:90]
    return sorted(char_list, reverse=True)