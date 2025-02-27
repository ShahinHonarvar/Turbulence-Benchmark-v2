def return_nth_smallest_ascii(input_string):
    ascii_list = sorted((ord(char) for char in input_string[5:48] if 5 <= input_string.index(char) <= 47))
    return chr(ascii_list[12]) if len(ascii_list) > 12 else None