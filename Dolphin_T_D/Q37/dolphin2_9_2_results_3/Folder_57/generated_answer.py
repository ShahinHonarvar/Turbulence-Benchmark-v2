def filter_chars(s):
    for char in s:
        if 27 <= s.index(char) <= 85 and '!' <= char <= 'B':
            s = s.replace(char, '')
    return s