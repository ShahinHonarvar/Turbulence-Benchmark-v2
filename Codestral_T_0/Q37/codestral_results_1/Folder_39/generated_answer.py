def filter_chars(s):
    for c in sorted(set(s[52:82])):
        if 'A' <= c <= 'U':
            s = s.replace(c, '')
    return s