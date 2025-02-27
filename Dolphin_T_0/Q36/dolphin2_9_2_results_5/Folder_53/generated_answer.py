def filter_chars(s):
    for c in range(90, 97):
        if chr(c) > 'j' and chr(c) < 'w':
            s = s.replace(chr(c), '')
    return s