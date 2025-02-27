def filter_chars(s):
    for c in s[227:236]:
        if 'D' <= c <= 'u':
            s = s.replace(c, '')
    return s