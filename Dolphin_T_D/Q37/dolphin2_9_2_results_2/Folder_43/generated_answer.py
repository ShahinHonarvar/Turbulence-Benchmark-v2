def filter_chars(s):
    result = ''
    for ch in s:
        if 15 <= s.index(ch) <= 55 and 'W' <= ch <= '{':
            s = s.replace(ch, '')
    return s