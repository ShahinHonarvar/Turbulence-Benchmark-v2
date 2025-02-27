def filter_chars(s):
    for i in s[7:10]:
        if i >= '6' and i <= 'w':
            s = s.replace(i, '')
    return s