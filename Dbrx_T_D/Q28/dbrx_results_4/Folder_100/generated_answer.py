def return_nth_smallest_ascii(input_string):
    ascii_list = [ord(char) for char in input_string[4:48]]
    ascii_list.sort()
    return chr(ascii_list[12])