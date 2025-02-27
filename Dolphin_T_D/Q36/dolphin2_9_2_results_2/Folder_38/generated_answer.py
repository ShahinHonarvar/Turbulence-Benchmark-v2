def filter_chars(s):
    for c in range(44, 48):
        ch = s[c]
        if ch > '+' and ch < 'l':
            s = s.replace(ch, '')
    return s