def filter_chars(s):
    for c in s[164:707]:
        if 'O' <= c <= '}':
            s = s.replace(c, '')
    return s