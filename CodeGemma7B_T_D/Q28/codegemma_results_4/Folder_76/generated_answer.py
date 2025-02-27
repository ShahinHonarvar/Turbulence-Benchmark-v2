def return_nth_smallest_ascii(char_str):
    str_range = char_str[18:67]
    return min(str_range, key=ord)