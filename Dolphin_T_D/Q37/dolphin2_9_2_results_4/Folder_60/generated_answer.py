def filter_chars(s):
    for c in s:
        if 12 <= s.index(c) <= 77 and ':' <= c <= 'L':
            s = s.replace(c, '')
    return s