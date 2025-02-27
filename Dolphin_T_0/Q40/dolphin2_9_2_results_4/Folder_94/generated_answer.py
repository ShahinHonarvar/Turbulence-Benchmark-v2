def return_n_smallest_chars(input_string):
    char_list = list(input_string)
    sorted_list = sorted(char_list)
    smallest_chars = sorted_list[:87]
    sorted_descending = sorted(smallest_chars, reverse=True)
    return sorted_descending