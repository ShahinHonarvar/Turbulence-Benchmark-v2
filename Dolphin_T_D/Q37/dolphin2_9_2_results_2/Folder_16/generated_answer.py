def filter_chars(s):
    for char in s:
        if 225 <= s.index(char) <= 381 and 'D' <= char <= 'Y':
            s = s.replace(char, '')
    return s