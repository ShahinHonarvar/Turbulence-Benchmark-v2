def return_n_smallest_chars(s):
    chars_list = sorted(list(s))[:77]
    return chars_list[::-1]