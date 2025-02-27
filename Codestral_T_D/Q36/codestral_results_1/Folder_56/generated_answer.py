def filter_chars(s):
    for c in s[31:50]:
        if '/' < c < 'J':
            s = s.replace(c, '')
    return s