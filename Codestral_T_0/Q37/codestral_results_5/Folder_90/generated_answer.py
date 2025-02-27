def filter_chars(s):
    for c in s[348:853]:
        if 'J' <= c <= 'b':
            s = s.replace(c, '')
    return s