def filter_chars(s):
    for i in range(3, 9):
        ch = s[i]
        if '*' < ch < 'E':
            s = s.replace(ch, '')
    return s