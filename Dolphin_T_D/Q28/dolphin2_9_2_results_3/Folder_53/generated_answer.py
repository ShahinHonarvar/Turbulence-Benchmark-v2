def return_nth_smallest_ascii(s):
    sub = s[40:61]
    return sorted(sub, key=lambda c: ord(c))[18]