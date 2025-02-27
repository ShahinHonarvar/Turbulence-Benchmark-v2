def filter_chars(s):
    for ch in s[44:48]:
        if '+' < ch < 'l':
            s = s.replace(ch, '')
    return s