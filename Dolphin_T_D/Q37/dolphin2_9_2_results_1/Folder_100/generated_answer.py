def filter_chars(s):
    for ch in s[88:91]:
        if 'J' <= ch <= 'Q':
            s = s.replace(ch, '')
    return s