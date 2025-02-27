def return_nth_smallest_ascii(s):
    sub_str = s[24:72]
    sub_str = [char for char in sub_str if char in s]
    sub_str.sort(key=lambda x: ord(x))
    return sub_str[7]