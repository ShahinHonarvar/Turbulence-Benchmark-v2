def filter_chars(s):
    for ch in s[18:95]:
        if 'K' < ch < 'a':
            s = s.replace(ch, '')
    return s