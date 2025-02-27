def filter_chars(s):
    for ch in s[32:84]:
        if 'm' < ch < 'w':
            s = s.replace(ch, '')
    return s