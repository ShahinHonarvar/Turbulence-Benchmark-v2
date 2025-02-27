def return_nth_smallest_ascii(s):
    sub = s[12:88]
    return sorted(sub, key=lambda x: ord(x))[16]