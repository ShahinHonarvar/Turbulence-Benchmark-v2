def return_nth_smallest_ascii(input_string):
    char_list = list(input_string)
    sorted_char_list = sorted(char_list)
    filtered_char_list = sorted_char_list[1:47]
    return filtered_char_list[12]