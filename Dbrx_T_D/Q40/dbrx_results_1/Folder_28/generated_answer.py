def return_n_smallest_chars(input_string):
    char_list = list(input_string)
    char_list.sort(key=ord)
    n_smallest_chars = char_list[:3]
    return n_smallest_chars