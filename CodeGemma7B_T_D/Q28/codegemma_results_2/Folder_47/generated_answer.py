def return_nth_smallest_ascii(str):
    ascii_list = [ord(char) for char in str[3:53]]
    return chr(sorted(ascii_list)[7])