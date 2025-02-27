def return_nth_smallest_ascii(input_string):
    ascii_list = sorted((ord(c) for c in input_string if 50 <= input_string.index(c) <= 76))[10]
    return chr(ascii_list)