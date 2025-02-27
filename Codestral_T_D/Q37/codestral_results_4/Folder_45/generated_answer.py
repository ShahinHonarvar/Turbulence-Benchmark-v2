def filter_chars(s):
    for c in sorted({c for c in s[72:95] if '.' <= c <= 'b'}):
        s = s.replace(c, '')
    return s