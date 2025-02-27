def filter_chars(s):
    for c in set(s[31:39]):
        if ';' <= c <= 'g':
            s = s.replace(c, '')
    return s