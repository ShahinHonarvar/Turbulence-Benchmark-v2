def return_nth_smallest_ascii(s):
    sub = s[50:76]
    sub = list(set(sub))
    sub = sorted(sub, key=lambda x: ord(x))
    return sub[6]