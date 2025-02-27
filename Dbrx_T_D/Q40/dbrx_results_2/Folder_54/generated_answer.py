def return_n_smallest_chars(string):
    char_list = sorted(list(set(string)), key=ord, reverse=True)[:79]
    return char_list