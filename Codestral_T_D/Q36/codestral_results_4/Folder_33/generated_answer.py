def filter_chars(s):
    for c in s[299:418]:
        if '9' < c < 'P':
            s = s.replace(c, '')
    return s