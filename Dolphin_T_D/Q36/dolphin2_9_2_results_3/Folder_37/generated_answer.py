def filter_chars(s):
    for i in range(44, 59):
        ch = s[i]
        if '\\' < ch < '6':
            s = s.replace(ch, '')
    return s