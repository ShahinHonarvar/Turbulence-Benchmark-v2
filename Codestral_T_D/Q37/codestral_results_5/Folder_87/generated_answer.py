def filter_chars(s):
    for char in [c for c in s[18:82] if 'W' <= c < '[']:
        s = s.replace(char, '')
    return s