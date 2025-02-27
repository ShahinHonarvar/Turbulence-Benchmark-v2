def filter_chars(s):
    for c in s:
        if 5 <= s.index(c) <= 6 and 'G' <= c <= 'p':
            s = s.replace(c, '')
    return s