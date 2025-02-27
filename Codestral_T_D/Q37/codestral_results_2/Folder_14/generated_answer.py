def filter_chars(s):
    for c in s[35:99]:
        if 'A' <= c <= 'b':
            s = s.replace(c, '')
    return s