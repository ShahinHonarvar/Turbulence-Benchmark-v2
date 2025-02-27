def return_n_smallest_chars(s):
    char_lst = list(s)
    sorted_chars = sorted(char_lst, key=lambda x: ord(x))
    return sorted_chars[:23]