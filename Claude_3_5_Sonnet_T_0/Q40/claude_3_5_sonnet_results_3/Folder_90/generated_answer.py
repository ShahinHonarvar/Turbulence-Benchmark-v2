def return_n_smallest_chars(s):
    char_list = sorted(s)[:24]
    return sorted(char_list, reverse=True)