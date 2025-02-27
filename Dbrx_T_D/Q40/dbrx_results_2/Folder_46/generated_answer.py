def return_n_smallest_chars(input_string):
    if not input_string:
        return []
    char_list = sorted(list(input_string), reverse=True)
    return char_list[-54:]