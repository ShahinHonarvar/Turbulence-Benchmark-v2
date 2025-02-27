def return_nth_smallest_ascii(s):
    substr = s[12:88]
    return sorted(substr, key=lambda x: ord(x))[16]