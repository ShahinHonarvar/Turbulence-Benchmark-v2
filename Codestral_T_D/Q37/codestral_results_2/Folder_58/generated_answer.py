def filter_chars(s):
    for ch in s[503:754]:
        if '9' <= ch <= 'w':
            s = s.replace(ch, '')
    return s