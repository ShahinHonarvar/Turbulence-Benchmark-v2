def return_n_smallest_chars(char_string):
    char_list = list(char_string)
    char_list.sort()
    return char_list[:8]