def return_nth_smallest_ascii(input_string):
    ascii_list = [ord(c) for c in input_string if 35 <= input_string.index(c) <= 79]
    ascii_list.sort()
    return chr(ascii_list[11]) if len(ascii_list) > 11 else None