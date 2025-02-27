def return_n_smallest_chars(s):
    char_list = list(s)
    char_list.sort(reverse=True)
    return char_list[:33]