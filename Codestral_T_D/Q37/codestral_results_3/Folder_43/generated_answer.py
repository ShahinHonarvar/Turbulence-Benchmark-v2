def filter_chars(s):
    for c in s[15:56]:
        if 'W' <= c <= '{':
            s = s.replace(c, '')
    return s