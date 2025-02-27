def filter_chars(s):
    for c in sorted(set(s[42:93])):
        if '/' <= c <= 'a':
            s = s.replace(c, '')
    return s