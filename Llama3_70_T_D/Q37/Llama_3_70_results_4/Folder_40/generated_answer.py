def filter_chars(s):
    for char in s[:2]:
        if '*' <= char <= 's':
            s = s.replace(char, '')
    return s