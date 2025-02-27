def filter_chars(s):
    for c in s:
        if 26 <= s.index(c) <= 64 and 'V' <= c <= 'o':
            s = s.replace(c, '')
    return s