def filter_chars(s):
    for ch in s[318:337]:
        if 'B' < ch < 'z':
            s = s.replace(ch, '')
    return s