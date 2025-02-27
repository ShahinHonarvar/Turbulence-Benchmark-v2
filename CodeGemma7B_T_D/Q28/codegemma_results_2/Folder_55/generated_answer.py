def return_nth_smallest_ascii(char_string):
    sliced_string = char_string[0:13]
    return min(sliced_string, key=ord)