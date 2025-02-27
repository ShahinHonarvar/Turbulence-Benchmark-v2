def return_nth_smallest_ascii(my_string):
    sub_string = my_string[10:74]
    ascii_list = [ord(char) for char in sub_string]
    ascii_list.sort()
    return chr(ascii_list[8])