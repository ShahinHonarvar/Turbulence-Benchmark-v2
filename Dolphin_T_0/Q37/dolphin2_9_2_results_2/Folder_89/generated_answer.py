def filter_chars(s):
    for char in s:
        if 11 <= s.index(char) <= 32 and '!' <= char <= '@':
            s = s.replace(char, '')
    return s