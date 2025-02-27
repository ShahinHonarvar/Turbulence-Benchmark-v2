def return_n_smallest_chars(input_string):
    char_list = list(input_string)
    char_list.sort()
    sorted_chars = sorted(char_list, key=lambda x: ord(x))
    return sorted_chars[:6]