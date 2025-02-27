def filter_chars(s):
    for c in s[42:78]:
        if '!' < c < '?':
            s = s.replace(c, '')
    return s