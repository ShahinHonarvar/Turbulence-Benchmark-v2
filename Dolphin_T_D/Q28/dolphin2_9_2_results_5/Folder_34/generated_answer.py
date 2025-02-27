def return_nth_smallest_ascii(s):
    substr = s[0:19]
    ascii_list = [ord(c) for c in substr]
    ascii_list.sort()
    return chr(ascii_list[18])