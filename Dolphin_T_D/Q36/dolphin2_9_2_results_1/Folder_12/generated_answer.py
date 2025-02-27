def filter_chars(s):
    m = 'm'
    w = 'w'
    for char in range(32, 84):
        if m < chr(char) < w:
            s = s.replace(chr(char), '')
    return s