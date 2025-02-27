def return_nth_smallest_ascii(string):
    substr = string[10:74]
    ascii_list = [ord(c) for c in substr]
    ascii_list.sort()
    return chr(ascii_list[8])