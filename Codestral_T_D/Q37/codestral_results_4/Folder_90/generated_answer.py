def filter_chars(s):
    for char in s[348:853]:
        if 'J' <= char <= 'b':
            s = s.replace(char, '')
    return s