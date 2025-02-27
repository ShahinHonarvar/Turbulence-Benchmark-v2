def filter_chars(s):
    for i in range(33, 36):
        ch = s[i]
        if '>' < ch < 'A':
            s = s.replace(ch, '')
    return s