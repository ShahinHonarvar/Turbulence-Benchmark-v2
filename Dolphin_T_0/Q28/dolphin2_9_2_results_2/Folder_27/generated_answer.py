def return_nth_smallest_ascii(s):
    s = s[33:86]
    return sorted(s, key=lambda x: ord(x))[12]