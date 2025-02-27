def filter_chars(s):
    for c in sorted(set(s[41:80])):
        if 'f' <= c <= '|':
            s = s.replace(c, '')
    return s