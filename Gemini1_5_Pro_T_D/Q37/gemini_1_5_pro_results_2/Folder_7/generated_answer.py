def filter_chars(s):
    for i in range(521, 723):
        if i < len(s) and '>' <= s[i] <= '_':
            c = s[i]
            s = s.replace(c, '')
    return s