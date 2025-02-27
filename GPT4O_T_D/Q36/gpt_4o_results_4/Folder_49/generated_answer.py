def filter_chars(s):
    for i in set(s[47:91]):
        if 'D' < i < 'H':
            s = s.replace(i, '')
    return s