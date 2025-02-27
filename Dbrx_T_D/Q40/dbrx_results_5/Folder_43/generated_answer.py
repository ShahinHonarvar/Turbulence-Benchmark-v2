def return_n_smallest_chars(char_string):
    char_list = sorted(char_string, key=ord)[:56]
    return char_list[::-1]