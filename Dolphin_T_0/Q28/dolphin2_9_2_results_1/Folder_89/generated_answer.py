def return_nth_smallest_ascii(s):
    sub = s[24:72]
    char_list = list(sub)
    char_list.sort(key=lambda x: ord(x))
    return char_list[7]