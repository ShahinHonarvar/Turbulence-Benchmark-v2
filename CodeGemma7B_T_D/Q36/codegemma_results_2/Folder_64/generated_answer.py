def filter_chars(s):
    for i in range(1, 7):
        c = s[i]
        if c > '3' and c < '^':
            while c in s:
                s = s.replace(c, '', 1)
    return s