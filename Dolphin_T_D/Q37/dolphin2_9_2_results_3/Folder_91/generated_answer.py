def filter_chars(s):
    for char in s:
        if 7 <= s.index(char) <= 8 and 'B' <= char <= 'H':
            s = s.replace(char, '')
    return s