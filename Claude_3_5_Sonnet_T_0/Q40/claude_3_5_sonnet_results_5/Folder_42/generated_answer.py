def return_n_smallest_chars(s):
    char_list = sorted(s)[:59]
    return sorted(char_list, reverse=True)