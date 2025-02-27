def return_nth_smallest_ascii(input_string):
    ascii_list = [ord(c) for c in input_string if 38 <= input_string.index(c) <= 82]
    ascii_list.sort()
    return chr(ascii_list[19]) if len(ascii_list) > 19 else None