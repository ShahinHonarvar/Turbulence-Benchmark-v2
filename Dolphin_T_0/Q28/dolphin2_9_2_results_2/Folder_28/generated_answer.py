def return_nth_smallest_ascii(s):
    sub_s = s[25:78]
    sub_s = list(sub_s)
    sub_s.sort(key=lambda x: ord(x))
    return sub_s[15]