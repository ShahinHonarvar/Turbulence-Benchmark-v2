def filter_chars(s):
    for char in [c for c in s[114:640] if '!' <= c <= 'x']:
        s = s.replace(char, '')
    return s