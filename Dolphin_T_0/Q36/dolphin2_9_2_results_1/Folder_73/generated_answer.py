def filter_chars(s):
    for c in s[66:90]:
        if c > '#' and c < 'T':
            s = s.replace(c, '')
    return s