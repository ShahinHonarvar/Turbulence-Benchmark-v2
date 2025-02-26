def return_n_smallest_chars(input_string):
    char_list = list(set(input_string))
    sorted_chars = sorted(char_list, key=lambda x: ord(x))
    smallest_13 = sorted_chars[:13]
    return sorted(smallest_13, reverse=True)