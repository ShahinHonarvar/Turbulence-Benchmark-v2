def filter_chars(s):
    for ch in s[55:66]:
        if 'f' < ch < '|':
            s = s.replace(ch, '')
    return s