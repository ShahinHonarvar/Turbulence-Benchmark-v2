def return_nth_smallest_ascii(s):
    sub = s[42:60]
    return sorted(sub, key=lambda c: ord(c))[16]