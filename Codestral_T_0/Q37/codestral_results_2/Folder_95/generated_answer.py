def filter_chars(s):
    for c in s[35:41]:
        if ')' <= c <= 'l':
            s = s.replace(c, '')
    return s