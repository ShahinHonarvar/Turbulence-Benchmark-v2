def return_n_smallest_chars(char_list):
    return sorted(char_list, key=ord)[:8]