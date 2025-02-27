def filter_chars(s):
    for i in range(37, 57):
        if i < len(s):
            if s[i] >= '6' and s[i] <= '_':
                c = s[i]
                s = s.replace(c, '')
    return s