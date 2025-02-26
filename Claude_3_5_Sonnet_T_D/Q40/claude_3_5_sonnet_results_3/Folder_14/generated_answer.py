def return_n_smallest_chars(s):
    char_list = sorted(set(s))[:69]
    return char_list.ljust(69, chr(127))[:69]