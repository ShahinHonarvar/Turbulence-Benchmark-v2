def filter_chars(s):
    for char in s:
        if 71 <= s.index(char) <= 94 and 'K' <= char <= 'a':
            s = s.replace(char, '')
    return s