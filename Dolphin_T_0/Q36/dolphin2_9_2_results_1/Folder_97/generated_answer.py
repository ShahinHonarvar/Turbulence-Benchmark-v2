def filter_chars(s):
    for c in range(ord('S') + 1, ord('m')):
        s = s.replace(chr(c), '')
    return s