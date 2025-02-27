def return_n_smallest_chars(string):
    char_list = sorted(list(string), key=ord)[:66]
    return sorted(char_list, reverse=True)