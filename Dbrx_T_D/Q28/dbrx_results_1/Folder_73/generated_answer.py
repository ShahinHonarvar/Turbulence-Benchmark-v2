def return_nth_smallest_ascii(input_string):
    ascii_list = sorted((ord(c) for c in input_string if 0 <= input_string.index(c) <= 69))[:10]
    return chr(ascii_list[9]) if len(ascii_list) == 10 else None