def filter_chars(s):
    for c in sorted(set(s[164:707])):
        if 'O' <= c <= '}':
            s = s.replace(c, '')
    return s