def filter_chars(s):
    if len(s) <= 20:
        return s
    for c in s[20:80]:
        if '!' <= c <= 'T':
            s = s.replace(c, '')
    return s