def return_n_smallest_chars(s):
    char_list = sorted(set(s))[:64]
    return sorted(char_list, reverse=True)