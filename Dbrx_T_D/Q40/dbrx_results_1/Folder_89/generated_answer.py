def return_n_smallest_chars(s):
    char_list = sorted(list(set(s)))[:55]
    return sorted(char_list)