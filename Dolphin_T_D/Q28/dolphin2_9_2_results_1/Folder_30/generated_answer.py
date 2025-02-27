def return_nth_smallest_ascii(s):
    sub_s = s[50:77]
    return sorted(sub_s, key=lambda x: ord(x))[10]