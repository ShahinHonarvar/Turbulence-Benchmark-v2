def return_n_smallest_chars(s):
    char_list = sorted(list(set(s)))[:16]
    return sorted(char_list, reverse=True)