def filter_chars(s):
    for char in s[124:855]:
        if '9' <= char <= 's':
            s = s.replace(char, '')
    return s