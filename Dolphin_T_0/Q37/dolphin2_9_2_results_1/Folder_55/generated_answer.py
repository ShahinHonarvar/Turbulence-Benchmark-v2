def filter_chars(s):
    for c in s:
        if 1 <= s.index(c) <= 5 and '$' <= c <= ';':
            s = s.replace(c, '')
    return s