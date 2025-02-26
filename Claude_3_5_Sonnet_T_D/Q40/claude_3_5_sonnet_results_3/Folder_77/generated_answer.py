def return_n_smallest_chars(string):
    char_list = list(set(string))
    char_list.sort()
    return char_list[:47]