def filter_chars(s):
    for char in sorted(set(s[521:723])):
        if '>' <= char <= '_':
            s = s.replace(char, '')
    return s