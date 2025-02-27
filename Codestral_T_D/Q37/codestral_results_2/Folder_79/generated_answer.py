def filter_chars(s):
    for char in s[10:53]:
        if '@' <= char <= 'T':
            s = s.replace(char, '')
    return s