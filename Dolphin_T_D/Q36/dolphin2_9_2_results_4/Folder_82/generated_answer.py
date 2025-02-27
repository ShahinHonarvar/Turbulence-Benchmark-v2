def filter_chars(s):
    for c in range(69, 97):
        if chr(c) > 'V' and chr(c) < 'j':
            s = s.replace(chr(c), '')
    return s