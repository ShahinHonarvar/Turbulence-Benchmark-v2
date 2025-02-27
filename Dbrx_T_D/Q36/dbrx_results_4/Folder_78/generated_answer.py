def filter_chars(s):
    for i in range(len(s)):
        if 29 < i < 33:
            c = s[i]
            if '%' < c < 'a':
                s = s.replace(c, '', 1)
    return s