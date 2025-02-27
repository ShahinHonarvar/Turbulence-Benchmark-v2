def filter_chars(s):
    for c in sorted(set(s[11:73])):
        if 'i' <= c <= 'v':
            s = s.replace(c, '')
    return s