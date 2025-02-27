def return_n_smallest_chars(string_of_chars):
    char_list = list(string_of_chars)
    char_list.sort()
    char_list.reverse()
    n_smallest_chars = char_list[:85]
    return n_smallest_chars