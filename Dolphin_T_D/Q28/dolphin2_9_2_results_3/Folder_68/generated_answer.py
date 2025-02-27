def return_nth_smallest_ascii(s):
    s = s[0:11]
    return sorted(s, key=lambda x: ord(x))[10]