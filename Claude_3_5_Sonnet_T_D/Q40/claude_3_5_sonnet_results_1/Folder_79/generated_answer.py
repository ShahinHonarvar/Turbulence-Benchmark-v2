def return_n_smallest_chars(s):
    char_list = sorted(set(s))[:82]
    return sorted(char_list, reverse=True)