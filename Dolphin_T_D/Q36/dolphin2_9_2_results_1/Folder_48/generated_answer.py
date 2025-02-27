def filter_chars(s):
    for i in range(154, 222):
        for c in range(ord('A'), ord('f')):
            s = s.replace(chr(c), '')
    return s