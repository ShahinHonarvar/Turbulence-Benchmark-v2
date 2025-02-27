def filter_chars(s):
    for c in s[72:93]:
        if '<' < c < 'J':
            s = s.replace(c, '')
    return s