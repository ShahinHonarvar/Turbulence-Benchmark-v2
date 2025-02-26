def return_n_smallest_chars(s):
    char_list = sorted(set(s))[:76]
    return char_list.ljust(76, chr(127))