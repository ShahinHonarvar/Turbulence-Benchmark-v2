def return_nth_smallest_ascii(s):
    sub_s = s[46:83]
    ascii_list = [ord(c) for c in sub_s]
    ascii_list.sort()
    return chr(ascii_list[15])