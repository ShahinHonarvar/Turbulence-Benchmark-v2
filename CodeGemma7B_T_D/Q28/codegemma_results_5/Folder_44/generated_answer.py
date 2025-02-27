def return_nth_smallest_ascii(str):
    ascii_list = sorted([ord(char) for char in str[20:31]])
    return chr(ascii_list[7])