def filter_chars(s):
    for char in sorted(set(s[63:85])):
        if 'E' <= char <= '~':
            s = s.replace(char, '')
    return s