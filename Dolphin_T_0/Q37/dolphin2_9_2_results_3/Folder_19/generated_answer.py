def filter_chars(s):
    for c in s:
        if 35 <= s.index(c) <= 89 and 'E' <= c <= 't':
            s = s.replace(c, '')
    return s