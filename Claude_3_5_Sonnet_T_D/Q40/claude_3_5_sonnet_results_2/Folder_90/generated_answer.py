def return_n_smallest_chars(input_string):
    char_list = list(set(input_string))
    char_list.sort(key=ord)
    smallest_chars = char_list[:24]
    smallest_chars.sort(reverse=True)
    return smallest_chars