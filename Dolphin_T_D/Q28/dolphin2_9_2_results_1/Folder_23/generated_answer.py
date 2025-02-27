def return_nth_smallest_ascii(s):
    sub_s = s[29:48]
    return sorted(sub_s, key=lambda x: ord(x))[6]