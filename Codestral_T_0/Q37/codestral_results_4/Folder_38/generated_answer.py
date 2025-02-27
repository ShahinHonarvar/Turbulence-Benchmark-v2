def filter_chars(s):
    for c in sorted(set(s[24:80])):
        if 'a' <= c <= 'f':
            s = s.replace(c, '')
    return s