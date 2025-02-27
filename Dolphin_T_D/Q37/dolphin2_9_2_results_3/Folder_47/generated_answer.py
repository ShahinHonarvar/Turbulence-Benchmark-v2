def filter_chars(s):
    for ch in s[38:55]:
        if ':' <= ch <= 'r':
            s = s.replace(ch, '')
    return s