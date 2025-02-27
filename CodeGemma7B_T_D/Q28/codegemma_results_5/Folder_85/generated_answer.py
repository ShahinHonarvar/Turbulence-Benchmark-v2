def return_nth_smallest_ascii(string):
    ascii_list = sorted([ord(char) for char in string[17:87]])
    return chr(ascii_list[14])