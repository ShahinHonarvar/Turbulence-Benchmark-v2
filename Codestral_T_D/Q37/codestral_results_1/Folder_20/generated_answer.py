def filter_chars(s):
    for c in sorted(set(s[25:98])):
        if 'm' <= c <= 'w':
            s = s.replace(c, '')
    return s