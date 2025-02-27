def return_nth_smallest_ascii(s):
    sub = s[5:48]
    return sorted(sub, key=lambda c: ord(c))[12]