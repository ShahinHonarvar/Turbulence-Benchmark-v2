def return_nth_smallest_ascii(string):
    ascii_list = [ord(x) for x in string[60:84]]
    ascii_list.sort()
    return chr(ascii_list[13])