def filter_chars(s):
    for i in s[1:6]:
        if ',' < i < 'f':
            s = s.replace(i, '')
    return s