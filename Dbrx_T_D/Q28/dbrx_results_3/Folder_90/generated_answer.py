def return_nth_smallest_ascii(input_string):
    ascii_list = sorted((ord(c) for c in input_string[17:84] if c.isalnum()))
    return chr(ascii_list[4]) if len(ascii_list) > 4 else None