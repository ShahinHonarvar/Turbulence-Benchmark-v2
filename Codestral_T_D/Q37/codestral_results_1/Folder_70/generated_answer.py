def filter_chars(s):
    for c in s[515:539]:
        if '+' <= c <= '}':
            s = s.replace(c, '')
    return s