def filter_chars(s):
    for c in s[0:2]:
        if c >= '*' and c <= 's':
            s = s.replace(c, '')
    return s