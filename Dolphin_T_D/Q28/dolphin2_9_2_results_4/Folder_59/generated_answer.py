def return_nth_smallest_ascii(s):
    char_list = list(s)
    ascii_list = [ord(c) for c in char_list]
    sorted_ascii_list = sorted(ascii_list[0:12])
    nth_smallest_char = chr(sorted_ascii_list[11])
    return nth_smallest_char