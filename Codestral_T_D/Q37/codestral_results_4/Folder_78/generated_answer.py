def filter_chars(s):
    for char in [c for c in s[75:100] if '8' <= c <= 'e']:
        s = s.replace(char, '')
    return s