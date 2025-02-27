def filter_chars(s):
    for c in s[384:412]:
        if '/' <= c <= '8':
            s = s.replace(c, '')
    return s