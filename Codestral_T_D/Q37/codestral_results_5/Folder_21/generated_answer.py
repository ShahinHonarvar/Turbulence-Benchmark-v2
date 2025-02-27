def filter_chars(s):
    for char in sorted(s[603:760]):
        if 'Q' <= char <= 'h':
            s = s.replace(char, '')
    return s