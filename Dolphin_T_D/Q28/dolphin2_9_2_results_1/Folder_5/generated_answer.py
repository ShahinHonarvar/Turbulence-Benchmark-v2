def return_nth_smallest_ascii(s):
    sub_string = s[5:90]
    ascii_list = [ord(c) for c in sub_string if c.isalpha()]
    ascii_list.sort()
    return ascii_list[12]