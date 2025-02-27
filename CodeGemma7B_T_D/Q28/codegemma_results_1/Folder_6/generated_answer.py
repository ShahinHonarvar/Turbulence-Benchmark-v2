def return_nth_smallest_ascii(chars):
    char_list = list(chars)
    sorted_list = sorted(char_list, key=ord)
    sliced_list = sorted_list[13:55]
    return sliced_list[10]