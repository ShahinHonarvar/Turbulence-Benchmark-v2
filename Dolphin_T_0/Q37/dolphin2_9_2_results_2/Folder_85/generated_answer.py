def filter_chars(s):
    for char in s:
        if 28 <= ord(char) <= 65 and 'O' <= char <= 'd':
            s = s.replace(char, '')
    return s