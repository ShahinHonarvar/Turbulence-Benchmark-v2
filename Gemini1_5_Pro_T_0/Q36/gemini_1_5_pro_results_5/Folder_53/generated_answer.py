def filter_chars(s):
    for i in range(91, 97):
        if 'j' < chr(i) < 'w':
            s = s.replace(chr(i), '')
    return s