def filter_chars(s):
    for c in s:
        if 114 <= s.index(c) <= 639 and '!' <= c <= 'x':
            s = s.replace(c, '')
    return s