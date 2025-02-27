def filter_chars(s):
    for c in sorted(set(s[515:539])):
        if '+' <= c <= '}':
            s = s.replace(c, '')
    return s