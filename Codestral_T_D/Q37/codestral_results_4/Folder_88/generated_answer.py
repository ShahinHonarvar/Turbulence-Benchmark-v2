def filter_chars(s):
    for char in [c for c in s[69:81] if '@' <= c <= 'p']:
        s = s.replace(char, '')
    return s