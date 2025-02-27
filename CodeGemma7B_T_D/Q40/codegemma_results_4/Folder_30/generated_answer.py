def return_n_smallest_chars(given_str):
    char_list = list(given_str)
    char_list.sort(key=ord)
    return char_list[:72]