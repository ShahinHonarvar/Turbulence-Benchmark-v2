def filter_chars(s):
    for c in s[19:23]:
        if ']' <= c <= 't':
            s = s.replace(c, '')
    return s