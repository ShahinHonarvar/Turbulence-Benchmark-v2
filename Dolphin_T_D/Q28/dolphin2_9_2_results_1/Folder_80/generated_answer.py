def return_nth_smallest_ascii(s):
    substring = s[51:90]
    l = list(set(substring))
    l.sort(key=ord)
    return l[13]