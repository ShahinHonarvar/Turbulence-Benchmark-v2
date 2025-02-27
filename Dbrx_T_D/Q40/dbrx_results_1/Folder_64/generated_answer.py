def return_n_smallest_chars(s):
    char_list = sorted(s, key=ord)[:39]
    return sorted(char_list, reverse=True)