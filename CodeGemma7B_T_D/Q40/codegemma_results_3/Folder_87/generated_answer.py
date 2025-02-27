def return_n_smallest_chars(char_list):
    unique_chars = list(set(char_list))
    unique_chars.sort()
    return unique_chars[:24]