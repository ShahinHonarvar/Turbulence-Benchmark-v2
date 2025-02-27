def return_nth_smallest_ascii(string):
    sub_string = string[25:78]
    ascii_list = [ord(c) for c in sub_string]
    ascii_list.sort()
    return chr(ascii_list[15])