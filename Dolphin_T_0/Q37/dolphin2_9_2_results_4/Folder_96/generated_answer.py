def filter_chars(s):
    for char in s:
        if 86 <= s.index(char) <= 92 and '!' <= char <= 's':
            s = s.replace(char, '')
    return s