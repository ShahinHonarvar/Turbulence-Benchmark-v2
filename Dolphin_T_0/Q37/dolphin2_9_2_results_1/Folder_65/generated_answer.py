def filter_chars(s):
    for i in range(61, 71):
        ch = s[i]
        if ch >= '0' and ch <= '@':
            s = s.replace(ch, '')
    return s