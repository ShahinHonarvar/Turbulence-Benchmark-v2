def return_nth_smallest_ascii(input_string):
    ascii_list = [ord(char) for char in input_string if 50 <= input_string.index(char) <= 76]
    ascii_list.sort()
    return chr(ascii_list[10]) if len(ascii_list) >= 11 else None