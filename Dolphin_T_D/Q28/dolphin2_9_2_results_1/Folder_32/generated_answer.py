def return_nth_smallest_ascii(string):
    substring = string[14:67]
    ascii_list = [ord(char) for char in substring]
    ascii_list_sorted = sorted(ascii_list)
    return chr(ascii_list_sorted[7])