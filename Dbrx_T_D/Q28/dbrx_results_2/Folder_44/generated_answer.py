def return_nth_smallest_ascii(input_string):
    sub_string = input_string[20:31]
    ascii_list = [ord(char) for char in sub_string]
    ascii_list.sort()
    return chr(ascii_list[7])