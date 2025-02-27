def return_nth_smallest_ascii(s):
    sub = s[25:78]
    return sorted(sub, key=lambda x: ord(x))[15]