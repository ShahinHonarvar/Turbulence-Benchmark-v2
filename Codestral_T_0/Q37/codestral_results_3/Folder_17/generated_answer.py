def filter_chars(s):
    for c in s[27:30]:
        if ';' <= c <= 'b':
            s = s.replace(c, '')
    return s