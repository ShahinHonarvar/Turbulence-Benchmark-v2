def return_nth_smallest_ascii(str):
    ascii_list = sorted([ord(c) for c in str[3:53] if str[3:53].index(c) not in [0, 1, 2]])
    return chr(ascii_list[7])