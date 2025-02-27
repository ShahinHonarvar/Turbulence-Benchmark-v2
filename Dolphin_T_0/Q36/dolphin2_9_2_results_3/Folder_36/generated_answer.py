def filter_chars(s):
    for ch in s[283:484]:
        if 'l' < ch < 't':
            s = s.replace(ch, '')
    return s