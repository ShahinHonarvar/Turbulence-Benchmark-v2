def return_nth_smallest_ascii(a):
    s = sorted([ord(x) for x in a[51:89 + 1]])
    return chr(s[13])