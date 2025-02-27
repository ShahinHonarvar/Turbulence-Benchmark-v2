def filter_chars(s):
    for ch in s[35:90]:
        if 'E' <= ch <= 't':
            s = s.replace(ch, '')
    return s