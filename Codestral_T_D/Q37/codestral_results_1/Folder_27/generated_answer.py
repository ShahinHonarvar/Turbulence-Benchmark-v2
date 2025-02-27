def filter_chars(s):
    for c in set(s[43:81]):
        if '=' <= c <= 'E':
            s = s.replace(c, '')
    return s