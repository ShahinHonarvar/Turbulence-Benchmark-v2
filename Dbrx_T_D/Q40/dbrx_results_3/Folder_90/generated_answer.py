def return_n_smallest_chars(string):
    char_list = sorted(list(string))[:24]
    char_list.sort(reverse=True)
    return char_list