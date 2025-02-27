def return_n_smallest_chars(s):
    char_list = list(set(s))
    char_list.sort(key=ord)
    char_list.reverse()
    return char_list[:44]