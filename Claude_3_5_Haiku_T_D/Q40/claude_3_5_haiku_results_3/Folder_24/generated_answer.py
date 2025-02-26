def return_n_smallest_chars(s):
    char_list = sorted(list(s), key=lambda x: ord(x))[:32]
    return sorted(char_list, reverse=True)