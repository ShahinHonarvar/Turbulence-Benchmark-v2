def filter_chars(s):
    for c in s[4:8]:
        if '?' < c < 'k':
            s = s.replace(c, '')
    return s