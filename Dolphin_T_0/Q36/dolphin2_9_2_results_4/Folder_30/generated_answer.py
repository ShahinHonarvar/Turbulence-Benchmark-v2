def filter_chars(s):
    for c in range(ord('3') + 1, ord('I')):
        s = s.replace(chr(c), '')
    return s