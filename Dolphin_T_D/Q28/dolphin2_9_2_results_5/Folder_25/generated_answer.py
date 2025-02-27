def return_nth_smallest_ascii(s):
    sub = s[34:69]
    return sorted(sub, key=lambda c: ord(c))[5]