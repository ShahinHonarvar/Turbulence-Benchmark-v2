def filter_chars(s):
    for ch in s[15:56]:
        if 'W' <= ch <= '{':
            s = s.replace(ch, '')
    return s