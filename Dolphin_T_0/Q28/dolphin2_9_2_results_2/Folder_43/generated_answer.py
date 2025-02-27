def return_nth_smallest_ascii(s):
    sub = s[14:36]
    return sorted(sub, key=lambda x: ord(x))[10]