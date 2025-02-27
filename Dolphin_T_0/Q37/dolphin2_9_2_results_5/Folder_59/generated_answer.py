def filter_chars(s):
    for i in s[2:3]:
        if i >= '5' and i <= '_':
            s = s.replace(i, '')
    return s