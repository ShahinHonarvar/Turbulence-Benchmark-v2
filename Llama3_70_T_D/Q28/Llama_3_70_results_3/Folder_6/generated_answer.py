def return_nth_smallest_ascii(char_string):
    sliced_string = char_string[14:55]
    sorted_chars = sorted(sliced_string)
    return sorted_chars[10]