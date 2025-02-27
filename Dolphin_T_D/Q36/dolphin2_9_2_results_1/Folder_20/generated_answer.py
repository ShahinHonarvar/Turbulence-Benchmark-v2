def filter_chars(s):
    for ch in s[13:40]:
        if ':' < ch < 'C':
            s = s.replace(ch, '')
    return s