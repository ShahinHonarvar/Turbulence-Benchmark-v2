def return_nth_smallest_ascii(string):
    ascii_list = [ord(ch) for ch in string[34:82]]
    ascii_list.sort()
    return chr(ascii_list[11])