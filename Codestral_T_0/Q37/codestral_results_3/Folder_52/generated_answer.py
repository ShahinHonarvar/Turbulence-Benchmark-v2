def filter_chars(s):
    for c in sorted(set(s[54:84])):
        if 'j' <= c <= 'v':
            s = s.replace(c, '')
    return s