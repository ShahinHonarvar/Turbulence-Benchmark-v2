def return_nth_smallest_ascii(string):
    char_list = sorted([char for char in string if ord(char) >= ord('a') and ord(char) <= ord('z')], key=ord)
    return char_list[9]