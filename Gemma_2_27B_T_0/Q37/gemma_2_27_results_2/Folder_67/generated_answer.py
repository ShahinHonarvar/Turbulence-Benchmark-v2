def filter_chars(s):
    for i in range(19, 23):
        if i < len(s):
            c = s[i]
            if c >= ']' and c <= 't':
                s = s.replace(c, '')
    return s