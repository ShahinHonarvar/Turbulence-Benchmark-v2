def return_nth_smallest_ascii(char_string):
    sub_string = char_string[17:57]
    sorted_sub_string = sorted(sub_string)
    return sorted_sub_string[8]