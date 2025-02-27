def return_nth_smallest_ascii(s):
    s = s[33:86]
    s = [c for c in s]
    s.sort()
    return s[12]