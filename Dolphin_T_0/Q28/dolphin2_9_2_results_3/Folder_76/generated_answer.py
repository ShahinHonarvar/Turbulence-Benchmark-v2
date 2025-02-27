def return_nth_smallest_ascii(s):
    sub = s[18:67]
    ascii_list = [ord(c) for c in sub]
    ascii_list.sort()
    return chr(ascii_list[18])