def filter_chars(s):
    for ch in set(s[225:382]):
        if 'D' <= ch <= 'Y':
            s = s.replace(ch, '')
    return s