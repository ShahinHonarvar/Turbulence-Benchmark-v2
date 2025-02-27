def filter_chars(s):
    for i in range(1, 7):
        ch = s[i]
        if '>' < ch < 'L':
            s = s.replace(ch, '')
    return s