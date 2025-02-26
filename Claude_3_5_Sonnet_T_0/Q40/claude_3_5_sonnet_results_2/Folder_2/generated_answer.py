def return_n_smallest_chars(s):
    char_list = sorted(set(s))[:48]
    return char_list.ljust(48, chr(127))