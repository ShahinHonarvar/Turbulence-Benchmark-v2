def return_nth_smallest_ascii(input_string):
    ascii_list = [ord(char) for char in input_string if input_string.index(char) < 19]
    ascii_list.sort()
    return chr(ascii_list[18])