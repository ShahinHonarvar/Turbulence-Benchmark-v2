def filter_chars(s):
    for c in range(ord('9') + 1, ord('P')):
        s = s.replace(chr(c), '')
    return s