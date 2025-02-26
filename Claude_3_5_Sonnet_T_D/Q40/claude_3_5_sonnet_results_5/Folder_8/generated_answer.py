def return_n_smallest_chars(s):
    char_list = sorted(set(s))[:83]
    return char_list.ljust(83, chr(127))[:83]