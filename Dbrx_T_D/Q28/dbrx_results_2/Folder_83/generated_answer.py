def return_nth_smallest_ascii(char_list):
    ascii_list = [ord(c) for c in char_list[30:71] if char_list.index(c) == char_list[30:71].index(c)]
    ascii_list.sort()
    if len(ascii_list) >= 15:
        return chr(ascii_list[14])
    else:
        return None