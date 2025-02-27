def return_nth_smallest_ascii(str_input):
    string_slicing = str_input[17:84]
    ascii_list = [ord(char) for char in string_slicing]
    ascii_list.sort()
    return chr(ascii_list[4])