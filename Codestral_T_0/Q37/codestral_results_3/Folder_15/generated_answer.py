def filter_chars(s):
    for c in s[2:7]:
        if '?' <= c <= 'f':
            s = s.replace(c, '')
    return s