def return_nth_smallest_ascii(s):
    sub = s[9:23]
    return sorted(sub, key=lambda x: ord(x))[3]