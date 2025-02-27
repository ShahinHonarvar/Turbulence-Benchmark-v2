def return_nth_smallest_ascii(s):
    sub = s[17:86]
    return sorted(sub, key=lambda x: ord(x))[14]