def return_nth_smallest_ascii(input_string):
    ascii_list = [ord(char) for char in input_string if 0 <= input_string.index(char) <= 3]
    ascii_list.sort()
    return chr(ascii_list[4]) if len(ascii_list) > 4 else None