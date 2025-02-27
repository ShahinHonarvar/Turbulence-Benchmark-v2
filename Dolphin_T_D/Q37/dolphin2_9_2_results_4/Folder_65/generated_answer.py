def filter_chars(s):
    for i in s[61:71]:
        if i >= '0' and i <= '@':
            s = s.replace(i, '')
    return s