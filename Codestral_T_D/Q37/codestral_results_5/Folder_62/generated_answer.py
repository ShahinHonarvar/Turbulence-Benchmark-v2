def filter_chars(s):
    for char in sorted(set(s[10:70])):
        if 'I' <= char <= 'K':
            s = s.replace(char, '')
    return s