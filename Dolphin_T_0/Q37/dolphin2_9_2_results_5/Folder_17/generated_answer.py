def filter_chars(s):
    for char in s:
        if 27 <= s.index(char) <= 29 and ';' <= char <= 'b':
            s = s.replace(char, '')
    return s