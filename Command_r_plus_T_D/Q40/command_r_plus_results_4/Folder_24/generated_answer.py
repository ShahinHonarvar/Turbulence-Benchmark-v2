def return_n_smallest_chars(s):
    char_list = list(s)
    char_list.sort()
    smallest_chars = char_list[:32]
    smallest_chars.reverse()
    return smallest_chars