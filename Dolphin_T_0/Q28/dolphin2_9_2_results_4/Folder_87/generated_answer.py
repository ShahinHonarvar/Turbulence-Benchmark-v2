def return_nth_smallest_ascii(s):
    sub_s = s[29:34]
    ascii_list = list(map(ord, sub_s))
    ascii_list.sort()
    return chr(ascii_list[4])