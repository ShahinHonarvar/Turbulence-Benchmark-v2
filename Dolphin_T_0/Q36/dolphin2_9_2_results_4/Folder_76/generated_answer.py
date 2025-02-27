def filter_chars(s):
    for ch in s[669:888]:
        if 'B' < ch < 'Y':
            s = s.replace(ch, '')
    return s