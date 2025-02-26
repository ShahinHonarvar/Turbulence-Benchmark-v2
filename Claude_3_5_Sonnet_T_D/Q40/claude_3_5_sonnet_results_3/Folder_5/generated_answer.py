def return_n_smallest_chars(input_string):
    char_list = list(set(input_string))
    sorted_chars = sorted(char_list, key=lambda x: ord(x))
    result = sorted_chars[:46]
    return sorted(result, reverse=True)