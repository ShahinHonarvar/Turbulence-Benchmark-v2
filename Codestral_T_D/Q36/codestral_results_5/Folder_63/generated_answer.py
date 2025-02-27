def filter_chars(s):
    for c in s[26:80]:
        if '<' < c < '>':
            s = s.replace(c, '')
    return s