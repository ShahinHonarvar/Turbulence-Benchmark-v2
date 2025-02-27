def filter_chars(s):
    for c in sorted(set(s[86:93])):
        if '!' <= c <= 's':
            s = s.replace(c, '')
    return s