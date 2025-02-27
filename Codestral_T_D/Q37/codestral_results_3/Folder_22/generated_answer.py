def filter_chars(s):
    for c in s[33:71]:
        if '7' <= c <= 'k':
            s = s.replace(c, '')
    return s