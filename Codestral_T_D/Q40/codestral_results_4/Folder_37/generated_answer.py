def return_n_smallest_chars(input_str):
    char_list = list(input_str)
    char_list.sort(key=ord)
    smallest_chars = char_list[:26]
    smallest_chars.reverse()
    return smallest_chars