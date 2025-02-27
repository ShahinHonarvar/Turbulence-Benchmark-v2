def filter_chars(s):
    for ch in s[72:93]:
        if '>' < ch < 'J':
            s = s.replace(ch, '')
    return s