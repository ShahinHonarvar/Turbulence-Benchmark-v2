def return_nth_smallest_ascii(input_str):
    ascii_list = sorted((ord(c) for c in input_str if 0 <= input_str.index(c) <= 4))
    return chr(ascii_list[4]) if len(ascii_list) > 4 else None