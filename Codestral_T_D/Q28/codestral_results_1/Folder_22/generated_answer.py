def return_nth_smallest_ascii(char_string):
    sorted_chars = sorted(char_string[0:17], key=ord)
    return sorted_chars[16]