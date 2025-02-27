def filter_chars(s):
    for i in range(35, 98, 1):
        ch = chr(i)
        if ch >= 'A' and ch <= 'b':
            for j in range(s.count(ch)):
                s = s.replace(ch, '', 1)
    return s