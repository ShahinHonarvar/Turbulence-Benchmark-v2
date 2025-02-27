def return_nth_smallest_ascii(input_string):
    sub_string = input_string[22:75]
    ascii_list = sorted((ord(c) for c in sub_string if c.isalpha()))
    return chr(ascii_list[11]) if len(ascii_list) > 11 else None