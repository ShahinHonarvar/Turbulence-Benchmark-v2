def return_n_smallest_chars(input_string):
    char_list = list(set(input_string))
    sorted_chars = sorted(char_list, key=lambda x: ord(x))
    smallest_65_chars = sorted_chars[:65]
    return sorted(smallest_65_chars, reverse=True)