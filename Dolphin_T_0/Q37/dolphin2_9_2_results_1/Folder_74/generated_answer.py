def filter_chars(s):
    for ch in s[19:33]:
        if 'f' <= ch <= 'o':
            s = s.replace(ch, '')
    return s