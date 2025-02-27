def filter_chars(s):
    for c in s[11:33]:
        if '!' <= c <= '@':
            s = s.replace(c, '')
    return s