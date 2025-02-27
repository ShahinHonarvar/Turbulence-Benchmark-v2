def return_nth_smallest_ascii(string):
    str_set = set(string)
    ascii_list = sorted([ord(char) for char in str_set if 58 <= ord(char) <= 85])
    return chr(ascii_list[4])