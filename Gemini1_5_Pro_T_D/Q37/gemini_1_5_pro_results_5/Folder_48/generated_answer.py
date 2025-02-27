def filter_chars(s):
    for i in range(513, 878):
        if i <= len(s) - 1:
            if s[i] >= '?' and s[i] <= 'n':
                c = s[i]
                s = s.replace(c, '')
    return s