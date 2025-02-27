def filter_chars(s):
    for c in s[83:100]:
        if '*' <= c <= 'j':
            s = s.replace(c, '')
    return s