def filter_chars(s):
    for c in s[61:71]:
        if '0' <= c <= '@':
            s = s.replace(c, '')
    return s