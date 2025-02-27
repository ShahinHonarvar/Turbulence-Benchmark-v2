def filter_chars(s):
    for c in s[12:78]:
        if ':' <= c <= 'L':
            s = s.replace(c, '')
    return s