def return_n_smallest_chars(string_arg):
    char_list = sorted(list(string_arg), reverse=True)
    return char_list[:7]