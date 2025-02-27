def return_nth_smallest_ascii(s):
    sub = s[22:75]
    return sorted(sub, key=lambda c: ord(c))[11]