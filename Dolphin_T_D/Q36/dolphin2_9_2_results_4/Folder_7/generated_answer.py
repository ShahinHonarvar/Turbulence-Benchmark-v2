def filter_chars(s):
    for i in range(502, 946):
        ch = s[i]
        if ch > 'W' and ch < 'y':
            s = s.replace(ch, '')
    return s