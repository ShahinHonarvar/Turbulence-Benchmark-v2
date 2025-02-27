def filter_chars(s):
    for c in sorted(set(s[20:63])):
        if 'i' <= c <= 'k':
            s = s.replace(c, '')
    return s