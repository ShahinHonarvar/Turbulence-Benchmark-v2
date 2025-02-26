def return_n_smallest_chars(string):
    char_list = sorted(list(set(string)))[:63]
    return char_list