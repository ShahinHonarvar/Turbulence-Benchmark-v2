def return_n_smallest_chars(string):
    char_list = list(set(string))
    sorted_chars = sorted(char_list, key=ord)
    return sorted_chars[:7]