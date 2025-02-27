def return_n_smallest_chars(s):
    char_list = list(set(s))
    char_list.sort()
    smallest_chars = char_list[:68]
    smallest_chars.reverse()
    return smallest_chars