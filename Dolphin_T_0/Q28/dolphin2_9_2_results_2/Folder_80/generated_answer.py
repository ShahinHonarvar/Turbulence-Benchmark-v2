def return_nth_smallest_ascii(s):
    sub = s[51:90]
    return sorted(sub, key=lambda x: ord(x))[13]