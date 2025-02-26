def return_n_smallest_chars(input_string):
    char_list = sorted(set(input_string))[:87]
    return sorted(char_list, reverse=True)