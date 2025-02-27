def return_n_smallest_chars(string):
    chars_list = sorted(list(set(string)))
    return chars_list[:63]