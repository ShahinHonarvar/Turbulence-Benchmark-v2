def filter_chars(s):
    for char in s:
        if 83 <= s.index(char) <= 99 and '*' <= char <= 'j':
            s = s.replace(char, '')
    return s