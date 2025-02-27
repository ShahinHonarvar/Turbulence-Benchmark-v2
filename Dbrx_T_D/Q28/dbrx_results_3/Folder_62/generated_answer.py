def return_nth_smallest_ascii(char_string):
    ascii_list = [ord(char) for char in char_string if 51 <= char_string.index(char) <= 78]
    ascii_list.sort()
    return ascii_list[9]