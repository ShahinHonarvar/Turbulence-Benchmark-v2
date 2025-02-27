def filter_chars(s):
    for ch in s[283:484]:
        if ch > 'l' and ch < 't':
            s = s.replace(ch, '')
    return s