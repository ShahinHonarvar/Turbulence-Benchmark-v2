def filter_chars(s):
    for char in s:
        if 12 <= s.index(char) <= 25 and 'P' <= char <= 'x':
            s = s.replace(char, '')
    return s