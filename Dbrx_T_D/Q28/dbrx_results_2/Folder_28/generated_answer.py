def return_nth_smallest_ascii(char_string):
    ascii_list = [ord(char) for char in char_string if 25 <= char_string.index(char) <= 77]
    ascii_list.sort()
    return chr(ascii_list[15])