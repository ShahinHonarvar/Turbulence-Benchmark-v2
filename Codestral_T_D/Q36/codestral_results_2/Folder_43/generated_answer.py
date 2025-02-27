def filter_chars(s):
    for c in s[27:75]:
        if 'A' < c < 'i':
            s = s.replace(c, '')
    return s