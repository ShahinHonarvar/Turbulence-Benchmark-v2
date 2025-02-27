def return_nth_smallest_ascii(char_string):
    ascii_list = [ord(char) for char in set(char_string[18:46])]
    ascii_list.sort()
    return chr(ascii_list[6])