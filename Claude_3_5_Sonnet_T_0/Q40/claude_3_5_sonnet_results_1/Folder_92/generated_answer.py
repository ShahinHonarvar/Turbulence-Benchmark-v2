def return_n_smallest_chars(s):
    char_list = sorted(set(s))[:63]
    return char_list