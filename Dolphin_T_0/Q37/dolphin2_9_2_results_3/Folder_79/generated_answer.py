def filter_chars(s):
    for ch in s:
        if 10 <= s.index(ch) <= 52 and '@' <= ch <= 'T':
            s = s.replace(ch, '')
    return s