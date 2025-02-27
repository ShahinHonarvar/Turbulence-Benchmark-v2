def filter_chars(s):
    for c in range(ord('t') + 1, ord('x')):
        s = s.replace(chr(c), '')
    return s