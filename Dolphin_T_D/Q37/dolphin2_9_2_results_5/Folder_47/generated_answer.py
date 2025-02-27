def filter_chars(s):
    for i in range(38, 55):
        ch = s[i]
        if ch >= ':' and ch <= 'r':
            s = s.replace(ch, '')
    return s