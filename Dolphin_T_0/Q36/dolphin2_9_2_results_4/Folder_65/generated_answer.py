def filter_chars(s):
    for c in range(ord('F') + 1, ord('O')):
        s = s.replace(chr(c), '')
    return s