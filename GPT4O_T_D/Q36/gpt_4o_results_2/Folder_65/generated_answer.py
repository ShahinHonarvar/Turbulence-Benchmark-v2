def filter_chars(s):
    if len(s) <= 58:
        return s
    for c in s[59:82]:
        if 'F' < c < 'O':
            s = s.replace(c, '')
    return s