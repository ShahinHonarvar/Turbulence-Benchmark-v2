def filter_chars(s):
    for char in range(33, 84):
        if 'm' < chr(char) < 'w':
            s = s.replace(chr(char), '')
    return s