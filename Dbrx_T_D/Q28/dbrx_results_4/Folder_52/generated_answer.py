def return_nth_smallest_ascii(char_string):
    ascii_list = sorted((ord(c) for c in char_string[46:73]))
    return chr(ascii_list[14])