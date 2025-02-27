def return_nth_smallest_ascii(s):
    sub_string = s[29:34]
    return sorted(sub_string, key=lambda x: ord(x))[4]