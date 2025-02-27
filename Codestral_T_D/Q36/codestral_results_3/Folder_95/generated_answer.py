def filter_chars(s):
    for ch in s[56:86]:
        if '+' < ch < 'w':
            s = s.replace(ch, '')
    return s