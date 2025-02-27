def filter_chars(s):
    for char in range(72, 95):
        if chr(char) >= '.' and chr(char) <= 'b':
            s = s.replace(chr(char), '')
    return s