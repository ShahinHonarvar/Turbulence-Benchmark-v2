def return_nth_smallest_ascii(s):
    char_list = list(s)
    sorted_chars = sorted(char_list[60:84], key=lambda x: ord(x))
    return sorted_chars[13]