def filter_chars(s):
    for c in sorted(set(s[138:921])):
        if '6' <= c <= 'A':
            s = s.replace(c, '')
    return s