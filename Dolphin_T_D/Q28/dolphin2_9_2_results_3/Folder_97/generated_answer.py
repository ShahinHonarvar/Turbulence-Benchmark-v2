def return_nth_smallest_ascii(s):
    sub_string = s[15:22]
    return sorted(list(sub_string), key=lambda x: ord(x))[5]