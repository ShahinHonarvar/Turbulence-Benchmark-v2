def return_n_smallest_chars(input_string):
    char_list = list(set(input_string))
    sorted_chars = sorted(char_list, key=lambda x: ord(x))
    smallest_61 = sorted_chars[:61]
    return sorted(smallest_61, reverse=True)