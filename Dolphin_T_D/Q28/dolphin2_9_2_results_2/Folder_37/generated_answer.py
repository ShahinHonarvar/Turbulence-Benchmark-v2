def return_nth_smallest_ascii(s):
    sub = s[28:68]
    return sorted(sub, key=lambda x: ord(x))[14]