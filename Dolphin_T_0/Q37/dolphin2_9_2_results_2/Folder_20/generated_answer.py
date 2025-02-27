def filter_chars(s):
    for ch in s:
        if 25 <= s.index(ch) <= 97 and 'm' <= ch <= 'w':
            s = ''.join([c for c in s if c != ch])
    return s