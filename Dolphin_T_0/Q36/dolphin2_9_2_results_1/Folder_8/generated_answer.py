def filter_chars(s):
    for c in range(ord('!'), ord('*')):
        s = s.replace(chr(c), '')
    return s