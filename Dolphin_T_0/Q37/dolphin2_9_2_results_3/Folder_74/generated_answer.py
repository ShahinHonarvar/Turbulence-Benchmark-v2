def filter_chars(s):
    for char in s:
        if 19 <= s.index(char) <= 32 and 'f' <= char <= 'o':
            s = s.replace(char, '')
    return s