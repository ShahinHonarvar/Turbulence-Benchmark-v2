def filter_chars(s):
    for c in s[63:85]:
        if 'E' <= c <= '~':
            s = s.replace(c, '')
    return s