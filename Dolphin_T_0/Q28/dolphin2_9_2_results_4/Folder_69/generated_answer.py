def return_nth_smallest_ascii(s):
    ascii_list = [ord(c) for c in s[67:78]]
    ascii_list.sort()
    return chr(ascii_list[6])