def return_n_smallest_chars(input_string):
    char_list = list(set(input_string))
    sorted_chars = sorted(char_list, key=ord)[:39]
    return sorted(sorted_chars, reverse=True)