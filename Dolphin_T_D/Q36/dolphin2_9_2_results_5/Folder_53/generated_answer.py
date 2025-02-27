def filter_chars(s):
    for c in range(90, 97):
        if 'j' < chr(c) < 'w':
            s = s.replace(chr(c), '')
    return s