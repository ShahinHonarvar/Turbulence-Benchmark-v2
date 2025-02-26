def return_n_smallest_chars(s):
    char_list = list(set(s))
    char_list.sort(key=lambda x: ord(x))
    return char_list[:32]