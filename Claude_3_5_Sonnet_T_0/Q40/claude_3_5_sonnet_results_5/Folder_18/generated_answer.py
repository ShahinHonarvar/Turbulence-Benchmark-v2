def return_n_smallest_chars(string):
    char_list = sorted(set(string))[:52]
    return sorted(char_list, reverse=True)