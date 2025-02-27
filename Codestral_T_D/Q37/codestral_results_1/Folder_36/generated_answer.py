def filter_chars(s):
    for c in sorted(set(s[259:503])):
        if ',' <= c <= '3':
            s = s.replace(c, '')
    return s