def filter_chars(s):
    for c in s[49:56]:
        if 'I' < c < 'a':
            s = s.replace(c, '')
    return s