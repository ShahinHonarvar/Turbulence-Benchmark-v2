def return_nth_smallest_ascii(s):
    s = s[21:60]
    s = sorted(s, key=ord)
    return s[10]