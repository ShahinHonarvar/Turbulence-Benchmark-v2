def filter_chars(s):
    for char in s:
        if 'R' <= char <= 't' and 8 <= s.index(char) <= 9:
            s = s.replace(char, '')
    return s