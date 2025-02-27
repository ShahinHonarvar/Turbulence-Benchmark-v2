def filter_chars(s):
    for c in sorted(set(s[521:723])):
        if '>' <= c <= '_':
            s = s.replace(c, '')
    return s