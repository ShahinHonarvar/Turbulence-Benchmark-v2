def filter_chars(s):
    for c in s:
        if 35 <= s.index(c) <= 40 and ')' <= c <= 'l':
            s = s.replace(c, '')
    return s