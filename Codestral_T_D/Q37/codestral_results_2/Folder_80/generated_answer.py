def filter_chars(s):
    for c in s[36:80]:
        if 'a' <= c <= 'i':
            s = s.replace(c, '')
    return s