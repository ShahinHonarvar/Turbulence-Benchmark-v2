def return_nth_smallest_ascii(input_string):
    ascii_list = sorted((ord(c) for c in input_string[50:76] if c.islower()))
    return chr(ascii_list[6]) if len(ascii_list) >= 7 else None