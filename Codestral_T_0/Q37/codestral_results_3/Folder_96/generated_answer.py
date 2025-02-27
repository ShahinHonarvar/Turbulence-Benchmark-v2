def filter_chars(s):
    for c in s[86:93]:
        if '!' <= c <= 's':
            s = s.replace(c, '')
    return s