def return_n_smallest_chars(s):
    char_list = list(set(s))
    char_list.sort()
    return char_list[:66]