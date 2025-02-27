def return_n_smallest_chars(s):
    char_list = list(s)
    sorted_chars = sorted(char_list, key=lambda x: ord(x))
    return sorted_chars[:17]