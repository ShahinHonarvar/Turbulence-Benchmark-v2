def filter_chars(s):
    for c in s:
        if 17 <= s.index(c) <= 63 and 'O' <= c <= '^':
            s = ''.join([v for v in s if v != c])
    return s