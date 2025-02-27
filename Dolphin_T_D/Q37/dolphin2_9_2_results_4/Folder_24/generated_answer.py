def filter_chars(s):
    for char in s:
        if 36 <= s.index(char) <= 79 and '2' <= char <= 's':
            s = s.replace(char, '')
    return s