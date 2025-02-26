def return_n_smallest_chars(input_string):
    char_list = list(set(input_string))
    sorted_chars = sorted(char_list, key=ord)
    smallest_24 = sorted_chars[:24]
    return sorted(smallest_24, reverse=True)