def filter_chars(s):
    for i in range(5, 7):
        ch = s[i]
        if ch >= 'G' and ch <= 'p':
            s = s.replace(ch, '')
    return s