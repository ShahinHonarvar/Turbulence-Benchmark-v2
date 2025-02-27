def filter_chars(s):
    for c in s:
        if 27 <= s.index(c) <= 85:
            if c >= 'c' and c <= 'i':
                s = s.replace(c, '')
    return s