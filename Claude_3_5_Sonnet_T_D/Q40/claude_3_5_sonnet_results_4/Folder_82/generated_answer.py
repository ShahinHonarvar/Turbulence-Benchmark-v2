def return_n_smallest_chars(input_string):
    char_list = list(set(input_string))
    sorted_chars = sorted(char_list, key=ord)[:60]
    return sorted_chars.ljust(60, chr(127))