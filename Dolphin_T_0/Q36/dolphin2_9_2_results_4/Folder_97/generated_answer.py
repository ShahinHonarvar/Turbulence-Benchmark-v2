def filter_chars(s):
    for ch in s[309:591]:
        if ch > 'S' and ch < 'm':
            s = s.replace(ch, '')
    return s