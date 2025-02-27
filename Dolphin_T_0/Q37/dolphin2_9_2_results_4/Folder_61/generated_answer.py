def filter_chars(s):
    for char in s:
        if 5 <= s.index(char) <= 6 and 'G' <= char <= 'p':
            s = s.replace(char, '')
    return s