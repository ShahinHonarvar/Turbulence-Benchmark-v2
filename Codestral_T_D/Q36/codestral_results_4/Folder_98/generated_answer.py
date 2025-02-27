def filter_chars(s):
    for c in s[4:8]:
        if '1' < c < 'J':
            s = s.replace(c, '')
    return s