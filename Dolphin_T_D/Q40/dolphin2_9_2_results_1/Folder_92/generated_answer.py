def return_n_smallest_chars(s):
    chars_list = list(s)
    chars_list.sort()
    return chars_list[:63]