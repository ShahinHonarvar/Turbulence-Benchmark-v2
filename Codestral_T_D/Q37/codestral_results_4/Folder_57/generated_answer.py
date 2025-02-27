def filter_chars(s):
    for char in [c for c in s[27:86] if '!' <= c <= 'B']:
        s = s.replace(char, '')
    return s