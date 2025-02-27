def filter_chars(s):
    for ch in s:
        if '*' <= ch <= 's':
            s = s.replace(ch, '')
    return s