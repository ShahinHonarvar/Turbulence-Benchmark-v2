def filter_chars(s):
    for char in s:
        if 19 <= s.index(char) <= 22 and ']' <= char <= 't':
            s = s.replace(char, '')
    return s