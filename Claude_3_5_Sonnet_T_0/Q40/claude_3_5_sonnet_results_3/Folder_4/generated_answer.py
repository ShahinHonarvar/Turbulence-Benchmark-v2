def return_n_smallest_chars(s):
    char_list = sorted(set(s))[:90]
    return sorted(char_list, reverse=True)